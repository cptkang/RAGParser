"""Test script to verify poppler setup"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 60)
print("Testing Poppler Setup")
print("=" * 60)

# Test 1: Check if poppler is in PATH
poppler_bin = project_root / ".venv" / "poppler" / "poppler-24.08.0" / "Library" / "bin"
print(f"\n1. Poppler installation directory:")
print(f"   Path: {poppler_bin}")
print(f"   Exists: {poppler_bin.exists()}")

# Test 2: Import preprocessing pipeline (should auto-setup poppler)
print(f"\n2. Importing preprocessing pipeline...")
try:
    from src.preprocessing.pipeline import PreprocessingPipeline
    print(f"   [OK] Import successful")
except Exception as e:
    print(f"   [FAIL] Import failed: {e}")

# Test 3: Check PATH
print(f"\n3. Checking PATH environment variable:")
path_contains_poppler = "poppler-24.08.0" in os.environ.get("PATH", "")
print(f"   Poppler in PATH: {path_contains_poppler}")

# Test 4: Try running pdfinfo
print(f"\n4. Testing pdfinfo command:")
import subprocess
try:
    result = subprocess.run(
        ["pdfinfo", "-v"],
        capture_output=True,
        text=True,
        timeout=5
    )
    if result.returncode == 0:
        print(f"   [OK] pdfinfo works!")
        print(f"   Version: {result.stdout.split()[2]}")
    else:
        print(f"   [FAIL] pdfinfo failed with code: {result.returncode}")
except FileNotFoundError:
    print(f"   [FAIL] pdfinfo not found in PATH")
except Exception as e:
    print(f"   [FAIL] Error: {e}")

print("\n" + "=" * 60)
print("Test complete!")
print("=" * 60)
