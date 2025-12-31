# core/compile_check.py
import subprocess
import tempfile
import os

def py_compile_check(code: str) -> tuple[bool, str]:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        path = f.name

    try:
        r = subprocess.run(
            ["python", "-m", "py_compile", path],
            capture_output=True,
            text=True
        )
        if r.returncode != 0:
            return False, r.stderr
        return True, ""
    finally:
        os.remove(path)