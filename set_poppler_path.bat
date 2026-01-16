@echo off
REM Add poppler to PATH for the current session
set "POPPLER_PATH=%~dp0.venv\poppler\poppler-24.08.0\Library\bin"
set "PATH=%POPPLER_PATH%;%PATH%"
echo Poppler path added: %POPPLER_PATH%
echo.
echo Now you can run your Python scripts that require poppler.
echo Example: python examples\run_rag_example.py
