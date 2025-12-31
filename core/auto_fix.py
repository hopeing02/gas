# core/auto_fix.py
from core.validator import ast_check
from core.compile_check import py_compile_check
from core.claude_client import generate_code

MAX_RETRY = 3

def generate_with_retry(spec: dict) -> str:
    last_error = ""

    for i in range(MAX_RETRY):
        code = generate_code({
            **spec,
            "previous_error": last_error
        })

        ok, err = ast_check(code)
        if not ok:
            last_error = err
            continue

        ok, err = py_compile_check(code)
        if not ok:
            last_error = err
            continue

        return code  # ✅ 완전 통과

    raise RuntimeError(f"자동 수정 실패:\n{last_error}")
