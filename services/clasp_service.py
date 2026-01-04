import subprocess
import json

CLASP_TIMEOUT = 30  # 초

def run_cmd(cmd: list[str]) -> tuple[int, str, str]:
    """
    안전한 CLI 실행 헬퍼
    """
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=CLASP_TIMEOUT,
    )
    return proc.returncode, proc.stdout.strip(), proc.stderr.strip()

def deploy() -> str:
    """
    clasp deploy 실행
    """
    return _run([
        "clasp",
        "deploy",
        "--description",
        "AI verified deployment"
    ])


def clasp_push() -> None:
    code, out, err = run_cmd(["clasp", "push", "--force"])
    if code != 0:
        raise RuntimeError(f"clasp push failed: {err or out}")


def clasp_run_test() -> str:
    """
    __ai_test__ 실행하고 return 값 반환
    """
    code, out, err = run_cmd([
        "clasp",
        "run",
        "__ai_test__",
        "--json"
    ])

    if code != 0:
        raise RuntimeError(f"clasp run failed: {err or out}")

    # clasp --json 출력 파싱
    try:
        data = json.loads(out)
        return data.get("response", {}).get("result", "")
    except Exception:
        # fallback (json 안 나오는 경우)
        return out
