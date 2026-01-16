# src/llm/llama_service.py

from typing import List, Dict, Optional, Generator
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BaseLlamaService(ABC):
    """Llama 서비스 기본 클래스"""
    
    @abstractmethod
    def generate(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.1,
        **kwargs
    ) -> str:
        pass
    
    @abstractmethod
    def generate_stream(
        self,
        prompt: str,
        **kwargs
    ) -> Generator[str, None, None]:
        pass


class OllamaService(BaseLlamaService):
    """
    Ollama를 통한 Llama 모델 서비스
    
    설치: ollama pull llama3.1:8b
    """
    
    def __init__(
        self,
        model_name: str = "llama3.1:8b",
        base_url: str = "http://localhost:11434"
    ):
        """
        Args:
            model_name: Ollama 모델명
            base_url: Ollama 서버 URL
        """
        import requests
        
        self.model_name = model_name
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"
        
        # 연결 테스트
        try:
            response = requests.get(f"{base_url}/api/tags")
            available_models = [m['name'] for m in response.json().get('models', [])]
            
            if model_name not in available_models:
                logger.warning(f"Model {model_name} not found. Available: {available_models}")
                logger.info(f"Pulling model {model_name}...")
                self._pull_model(model_name)
            
            logger.info(f"Ollama service initialized: {model_name}")
            
        except Exception as e:
            raise ConnectionError(f"Cannot connect to Ollama at {base_url}: {e}")
    
    def _pull_model(self, model_name: str):
        """모델 다운로드"""
        import requests
        
        response = requests.post(
            f"{self.base_url}/api/pull",
            json={"name": model_name},
            stream=True
        )
        
        for line in response.iter_lines():
            if line:
                logger.info(f"Pulling: {line.decode()}")
    
    def generate(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.1,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        텍스트 생성
        """
        import requests
        
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens,
                "temperature": temperature,
                **kwargs
            }
        }
        
        if system_prompt:
            payload["system"] = system_prompt
        
        response = requests.post(self.api_url, json=payload)
        response.raise_for_status()
        
        return response.json()["response"]
    
    def generate_stream(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.1,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        스트리밍 생성
        """
        import requests
        import json
        
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": True,
            "options": {
                "num_predict": max_tokens,
                "temperature": temperature,
                **kwargs
            }
        }
        
        if system_prompt:
            payload["system"] = system_prompt
        
        response = requests.post(self.api_url, json=payload, stream=True)
        
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode())
                if not data.get("done", False):
                    yield data.get("response", "")


class LlamaCppService(BaseLlamaService):
    """
    llama-cpp-python을 통한 로컬 Llama 서비스
    
    더 세밀한 제어가 필요한 경우 사용
    """
    
    def __init__(
        self,
        model_path: str,
        n_ctx: int = 4096,
        n_gpu_layers: int = -1,  # -1 = 전체 GPU 사용
        n_threads: Optional[int] = None
    ):
        """
        Args:
            model_path: GGUF 모델 파일 경로
            n_ctx: 컨텍스트 크기
            n_gpu_layers: GPU 레이어 수
            n_threads: CPU 스레드 수
        """
        from llama_cpp import Llama
        
        self.llm = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_gpu_layers=n_gpu_layers,
            n_threads=n_threads,
            verbose=False
        )
        
        logger.info(f"Llama.cpp service initialized: {model_path}")
    
    def generate(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.1,
        **kwargs
    ) -> str:
        """
        텍스트 생성
        """
        output = self.llm(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=["</s>", "[/INST]"],
            **kwargs
        )
        
        return output["choices"][0]["text"]
    
    def generate_stream(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.1,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        스트리밍 생성
        """
        for output in self.llm(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=["</s>", "[/INST]"],
            stream=True,
            **kwargs
        ):
            yield output["choices"][0]["text"]


class VLLMService(BaseLlamaService):
    """
    vLLM을 통한 고성능 Llama 서비스
    
    대규모 배포 및 높은 처리량 필요시 사용
    """
    
    def __init__(
        self,
        model_name: str = "meta-llama/Llama-3.1-8B-Instruct",
        base_url: str = "http://localhost:8000"
    ):
        """
        Args:
            model_name: HuggingFace 모델명
            base_url: vLLM 서버 URL
        """
        from openai import OpenAI
        
        self.client = OpenAI(
            base_url=f"{base_url}/v1",
            api_key="dummy"  # vLLM은 API 키 불필요
        )
        self.model_name = model_name
        
        logger.info(f"vLLM service initialized: {model_name}")
    
    def generate(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.1,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        텍스트 생성
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            **kwargs
        )
        
        return response.choices[0].message.content
    
    def generate_stream(
        self,
        prompt: str,
        max_tokens: int = 1024,
        temperature: float = 0.1,
        system_prompt: Optional[str] = None,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        스트리밍 생성
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True,
            **kwargs
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content