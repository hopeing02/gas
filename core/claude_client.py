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
    Claude SDK 응답 구조 안전 파싱
    """
    if not resp.content:
        raise RuntimeError("Claude response has no content")

    block = resp.content[0]
    if hasattr(block, "text"):
        return block.text

    raise RuntimeError("Unexpected Claude response format")

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
