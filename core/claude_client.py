import os
from anthropic import Anthropic
from anthropic.types import Message

# 1️⃣ 환경변수 안전 처리 (Railway 필수)
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
if not CLAUDE_API_KEY:
    raise RuntimeError("CLAUDE_API_KEY environment variable is not set")

client = Anthropic(api_key=CLAUDE_API_KEY)

SYSTEM_PROMPT = (
    "You are a Google Apps Script expert.\n"
    "Do not modify triggers, scopes, or permissions.\n"
    "Only fix function bodies.\n"
    "You are a senior Python engineer.\n"
    "Rules:\n"
    "- Output ONLY valid Python code\n"
    "- No markdown\n"
    "- No explanation\n"
    "- Python 3.13 compatible\n"
    "- If an error is provided, fix only that error\n"
)

def _extract_text(resp: Message) -> str:
    """
    Claude 응답에서 모든 text block을 안전하게 추출
    (SDK 버전 / 모델 변경에도 안 터짐)
    """
    if not hasattr(resp, "content") or not resp.content:
        raise RuntimeError("Claude response has no content")

    texts = []

    for block in resp.content:
        # SDK 객체 형태
        if hasattr(block, "type") and block.type == "text" and hasattr(block, "text"):
            texts.append(block.text)

        # dict 형태 (호환)
        elif isinstance(block, dict) and block.get("type") == "text":
            texts.append(block.get("text", ""))

    if not texts:
        raise RuntimeError(
            f"No text block found in Claude response: {resp.content}"
        )

    return "\n".join(texts)


def generate_code(spec: str) -> str:
    """
    코드 생성 / 수정 공용 함수
    """
    resp = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": spec if isinstance(spec, str) else str(spec)
            }
        ],
        thinking={
            "type": "enabled",
            "budget_tokens": 2000
        }
    )

    return _extract_text(resp)

def fix_code(payload: str) -> str:
    return generate_code(payload)
