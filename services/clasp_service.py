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
    """
    __ai_test__ 실행 결과 반환
    """
    output = _run([
        "clasp",
        "run",
        "__ai_test__",
        "--json"
    ])

    try:
        data = json.loads(output)
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON from clasp:\n{output}")

    # GAS Execution API 결과 구조
    # { "result": { "response": { "result": "OK" } } }
    try:
        return data["result"]["response"]["result"]
    except KeyError:
        raise RuntimeError(f"Unexpected clasp response:\n{json.dumps(data, indent=2)}")
