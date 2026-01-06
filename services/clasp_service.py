import subprocess
import json
import os

def _run(cmd: list[str]) -> str:
    """
    clasp 명령 실행 + stdout/stderr 안전 캡처
    """
    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\n"
            f"STDERR:\n{result.stderr}"
        )

    return result.stdout.strip()


def clasp_push():
    return _run(["clasp", "push"])


def clasp_run_test() -> str:
    # 1️⃣ JSON 옵션 없이 실행
    output = _run([
        "clasp",
        "run",
        "__ai_test__"
    ])

    # 2️⃣ 출력 자체가 없는 경우
    if not output.strip():
        raise RuntimeError(
            "clasp run returned empty output.\n"
            "Possible causes:\n"
            "- Execution API not enabled\n"
            "- Invalid OAuth token\n"
            "- Headless environment limitation"
        )

    return output.strip()

def deploy() -> str:
    """
    GAS 배포 (새 Deployment 생성)
    """
    output = _run([
        "clasp",
        "deploy",
        "--description",
        "AI verified deployment"
    ])
    return output

