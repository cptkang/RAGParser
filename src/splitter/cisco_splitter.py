# src/splitter/cisco_splitter.py

from typing import List, Dict, Optional, Any
from dataclasses import dataclass
import re
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter
)
from langchain_core.documents import Document


@dataclass
class ChunkMetadata:
    """청크 메타데이터"""
    source: str
    chapter: str
    section: str
    page_range: str
    chunk_type: str  # text, cli_command, table, warning
    has_code: bool
    keywords: List[str]


class CiscoManualSplitter:
    """
    시스코 매뉴얼에 최적화된 텍스트 스플리터
    
    전략:
    1. Markdown 헤더 기반 1차 분할
    2. 의미 단위 2차 분할 (CLI 명령어, 테이블 보존)
    3. 적정 청크 크기 유지
    """
    
    # 시스코 매뉴얼 특화 구분자
    CISCO_SEPARATORS = [
        "\n## ",       # 섹션 구분
        "\n### ",      # 서브섹션 구분
        "\n```",       # 코드 블록 (앞에서 분리)
        "```\n",       # 코드 블록 (뒤에서 분리)
        "\n\n",        # 단락 구분
        "\n",          # 줄바꿈
        " ",           # 단어
    ]
    
    def __init__(
        self,
        chunk_size: int = 800,
        chunk_overlap: int = 100,
        min_chunk_size: int = 100,
        preserve_cli_blocks: bool = True
    ):
        """
        Args:
            chunk_size: 목표 청크 크기 (토큰 기준)
            chunk_overlap: 청크 간 오버랩
            min_chunk_size: 최소 청크 크기
            preserve_cli_blocks: CLI 명령어 블록 보존 여부
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.min_chunk_size = min_chunk_size
        self.preserve_cli_blocks = preserve_cli_blocks
        
        # 헤더 기반 분할기
        self.header_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "chapter"),
                ("##", "section"),
                ("###", "subsection"),
            ]
        )
        
        # 재귀적 문자 분할기
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=self.CISCO_SEPARATORS,
            length_function=self._token_length,
        )
    
    def _token_length(self, text: str) -> int:
        """토큰 길이 계산 (한글 고려)"""
        # 간단한 추정: 한글은 문자당 ~1.5토큰, 영어는 ~0.25토큰
        korean_chars = len(re.findall(r'[가-힣]', text))
        other_chars = len(text) - korean_chars
        return int(korean_chars * 1.5 + other_chars * 0.25)
    
    def split_document(
        self, 
        content: str,
        metadata: Optional[Dict] = None
    ) -> List[Document]:
        """
        문서를 청크로 분할
        
        Args:
            content: Markdown 형식 문서 내용
            metadata: 문서 메타데이터
            
        Returns:
            Document 리스트
        """
        metadata = metadata or {}
        
        # 1단계: CLI 블록 추출 및 보호
        content, cli_blocks = self._extract_cli_blocks(content)
        
        # 2단계: 헤더 기반 분할
        header_splits = self.header_splitter.split_text(content)
        
        # 3단계: 각 섹션을 적정 크기로 세분화
        final_chunks = []
        
        for split in header_splits:
            section_metadata = {
                **metadata,
                **split.metadata
            }
            
            section_text = split.page_content
            
            # 섹션이 충분히 작으면 그대로 사용
            if self._token_length(section_text) <= self.chunk_size:
                final_chunks.append(Document(
                    page_content=section_text,
                    metadata={
                        **section_metadata,
                        'chunk_type': 'text'
                    }
                ))
            else:
                # 큰 섹션은 추가 분할
                sub_chunks = self.text_splitter.split_text(section_text)
                for i, chunk in enumerate(sub_chunks):
                    final_chunks.append(Document(
                        page_content=chunk,
                        metadata={
                            **section_metadata,
                            'chunk_type': 'text',
                            'sub_chunk_index': i
                        }
                    ))
        
        # 4단계: CLI 블록을 독립 청크로 추가
        if self.preserve_cli_blocks:
            for i, cli_block in enumerate(cli_blocks):
                final_chunks.append(Document(
                    page_content=cli_block['content'],
                    metadata={
                        **metadata,
                        'chunk_type': 'cli_command',
                        'cli_index': i,
                        'context': cli_block.get('context', '')
                    }
                ))
        
        # 5단계: 후처리
        final_chunks = self._postprocess_chunks(final_chunks)
        
        return final_chunks
    
    def _extract_cli_blocks(self, content: str) -> tuple:
        """CLI 코드 블록 추출"""
        cli_blocks = []
        
        # 코드 블록 패턴
        code_pattern = r'```(?:cisco-ios|ios|cli)?\n(.*?)```'
        
        def replacer(match):
            cli_content = match.group(1).strip()
            
            # CLI 명령어인지 확인
            if self._is_cisco_cli(cli_content):
                # 앞의 컨텍스트 (설명) 추출 시도
                cli_blocks.append({
                    'content': cli_content,
                    'placeholder': f'[CLI_BLOCK_{len(cli_blocks)}]'
                })
                return f'[CLI_BLOCK_{len(cli_blocks)-1}]'
            return match.group(0)
        
        processed_content = re.sub(code_pattern, replacer, content, flags=re.DOTALL)
        
        return processed_content, cli_blocks
    
    def _is_cisco_cli(self, text: str) -> bool:
        """시스코 CLI 명령어 여부 확인"""
        cli_indicators = [
            r'^(Router|Switch|Device)[>#]',
            r'^\w+[>#]',
            r'^\w+\(config[^\)]*\)#',
            r'^show\s+',
            r'^interface\s+',
            r'^ip\s+(address|route)',
            r'^no\s+',
            r'^enable',
            r'^configure\s+terminal',
        ]
        
        for pattern in cli_indicators:
            if re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
                return True
        return False
    
    def _postprocess_chunks(
        self, 
        chunks: List[Document]
    ) -> List[Document]:
        """청크 후처리"""
        processed = []
        
        for chunk in chunks:
            content = chunk.page_content.strip()
            
            # 너무 작은 청크 필터링
            if self._token_length(content) < self.min_chunk_size:
                continue
            
            # 메타데이터 보강
            chunk.metadata['token_count'] = self._token_length(content)
            chunk.metadata['has_code'] = '```' in content or '[CLI_BLOCK_' in content
            chunk.metadata['keywords'] = self._extract_keywords(content)
            
            processed.append(chunk)
        
        return processed
    
    def _extract_keywords(self, text: str) -> List[str]:
        """시스코 관련 키워드 추출"""
        keywords = []
        
        keyword_patterns = [
            r'\b(VLAN|STP|RSTP|PVST)\b',
            r'\b(OSPF|EIGRP|BGP|RIP)\b',
            r'\b(ACL|access-list)\b',
            r'\b(QoS|CoS|DSCP)\b',
            r'\binterface\s+(Gi|Fa|Te|Eth)\S+',
            r'\b(trunk|access)\s+mode\b',
            r'\bip\s+address\b',
            r'\b(enable|configure|show|debug)\b',
        ]
        
        for pattern in keyword_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            keywords.extend(matches)
        
        return list(set(keywords))[:10]  # 최대 10개


class SemanticChunkEnhancer:
    """
    의미 기반 청크 품질 향상
    
    - 불완전한 문장 처리
    - CLI 명령어와 설명 연결
    - 컨텍스트 보존
    """
    
    def __init__(self):
        pass
    
    def enhance_chunk(self, chunk: Document, context: str = "") -> Document:
        """청크 품질 향상"""
        content = chunk.page_content
        
        # 1. 불완전한 시작 처리
        if not self._has_complete_start(content):
            content = f"(계속) {content}"
        
        # 2. 불완전한 끝 처리  
        if not self._has_complete_end(content):
            content = f"{content} (...)"
        
        # 3. CLI 블록에 컨텍스트 추가
        if chunk.metadata.get('chunk_type') == 'cli_command' and context:
            content = f"[설명: {context}]\n\n{content}"
        
        chunk.page_content = content
        return chunk
    
    def _has_complete_start(self, text: str) -> bool:
        """완전한 시작 여부"""
        # 문장 시작 패턴
        starts = [r'^[A-Z가-힣]', r'^#', r'^\d+\.', r'^-']
        return any(re.match(p, text.strip()) for p in starts)
    
    def _has_complete_end(self, text: str) -> bool:
        """완전한 끝 여부"""
        ends = ['.', '!', '?', ':', '```', '|']
        text = text.strip()
        return any(text.endswith(e) for e in ends)