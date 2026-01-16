# Poppler Setup for RAGParser

## What is Poppler?

Poppler is a PDF rendering library required by the `unstructured` package for high-resolution PDF layout analysis. It provides utilities for extracting text, tables, and structural information from PDF files.

## Installation Status

✓ Poppler has been installed locally in your project at:
```
.venv/poppler/poppler-24.08.0/Library/bin/
```

## How It Works

The poppler setup has been automatically integrated into your codebase:

1. **Automatic PATH Setup**: The following files now automatically add poppler to PATH when imported:
   - `src/preprocessing/pipeline.py`
   - `src/vectorstore/indexing_pipeline.py`

2. **No Manual Configuration Needed**: When you run your Python scripts, poppler will be automatically available.

## Usage

### Option 1: Direct Script Execution (Recommended)

Simply run your scripts as normal. The poppler path is set automatically:

```bash
python examples/run_rag_example.py
python src/vectorstore/indexing_pipeline.py
```

### Option 2: Using the Wrapper Script

If you want explicit confirmation that poppler is loaded:

```bash
python run_with_poppler.py examples/run_rag_example.py
```

### Option 3: Manual PATH Setup (for other scripts)

If you need to run other scripts that require poppler:

**Windows CMD:**
```cmd
set_poppler_path.bat
python your_script.py
```

**Git Bash / PowerShell:**
```bash
export PATH="/g/RAGParser/.venv/poppler/poppler-24.08.0/Library/bin:$PATH"
python your_script.py
```

## Verification

To verify poppler is working:

```bash
# Set the path
export PATH="/g/RAGParser/.venv/poppler/poppler-24.08.0/Library/bin:$PATH"

# Check version
pdfinfo -v
```

Expected output:
```
pdfinfo version 24.08.0
Copyright 2005-2024 The Poppler Developers - http://poppler.freedesktop.org
```

## Troubleshooting

### Error: "Unable to get page count. Is poppler installed and in PATH?"

This error occurs when poppler is not in the system PATH. Solutions:

1. **Restart your IDE/terminal** after installation
2. **Use the wrapper script**: `python run_with_poppler.py your_script.py`
3. **Manually add to PATH** using one of the methods above

### Poppler Not Found

If you see "Poppler not found" messages, the poppler directory may have been deleted. To reinstall:

```bash
# Download poppler
curl -L -o poppler-windows.zip "https://github.com/oschwartz10612/poppler-windows/releases/download/v24.08.0-0/Release-24.08.0-0.zip"

# Extract to .venv
powershell -Command "Expand-Archive -Path 'poppler-windows.zip' -DestinationPath '.venv/poppler' -Force"
```

## Alternative: System-Wide Installation

If you prefer a system-wide poppler installation:

### Using Chocolatey (requires admin)
```cmd
choco install poppler
```

### Manual Installation
1. Download from: https://github.com/oschwartz10612/poppler-windows/releases/
2. Extract to `C:\poppler`
3. Add `C:\poppler\Library\bin` to Windows System PATH

## Files Created

- `set_poppler_path.bat` - Batch script to set PATH on Windows
- `run_with_poppler.py` - Python wrapper to run scripts with poppler
- `POPPLER_SETUP.md` - This documentation

## Technical Details

Poppler provides these command-line utilities:
- `pdfinfo` - Extract PDF metadata
- `pdftotext` - Convert PDF to text
- `pdftoppm` - Convert PDF pages to images
- `pdfimages` - Extract images from PDF
- And more...

The `unstructured` library uses these utilities internally for PDF processing.
