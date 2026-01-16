"""
Wrapper script to run Python scripts with poppler in PATH
Usage: python run_with_poppler.py <script_path> [arguments]
Example: python run_with_poppler.py examples/run_rag_example.py
"""

import os
import sys
from pathlib import Path
import subprocess

def setup_poppler_path():
    """Add poppler to PATH"""
    project_root = Path(__file__).parent
    poppler_bin = project_root / ".venv" / "poppler" / "poppler-24.08.0" / "Library" / "bin"

    if poppler_bin.exists():
        # Add to PATH for this process and subprocesses
        os.environ["PATH"] = str(poppler_bin) + os.pathsep + os.environ.get("PATH", "")
        print(f"✓ Poppler path added: {poppler_bin}")
        return True
    else:
        print(f"✗ Poppler not found at: {poppler_bin}")
        print("Please run the installation script first.")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_with_poppler.py <script_path> [arguments]")
        print("Example: python run_with_poppler.py examples/run_rag_example.py")
        sys.exit(1)

    if not setup_poppler_path():
        sys.exit(1)

    # Get the script to run and its arguments
    script_path = sys.argv[1]
    script_args = sys.argv[2:]

    # Run the script
    print(f"\nRunning: {script_path} {' '.join(script_args)}\n")
    print("=" * 60)

    # Use subprocess to run the script with the modified environment
    result = subprocess.run(
        [sys.executable, script_path] + script_args,
        env=os.environ
    )

    sys.exit(result.returncode)
