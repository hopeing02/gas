import os
from anthropic import Anthropic
from anthropic.types import Message

# 1️⃣ 환경변수 안전 처리 (Railway 필수)
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
if not CLAUDE_API_KEY:
    raise RuntimeError("CLAUDE_API_KEY environment variable is not set")

client = Anthropic(api_key=CLAUDE_API_KEY)

SYSTEM_PROMPT = """
You are an expert Google Apps Script engineer.

STRICT RULES:
- Output ONLY Google Apps Script code (JavaScript)
- No markdown
- No explanation
- No comments outside code
- Do NOT modify triggers, scopes, or permissions
- Do NOT use advanced services unless explicitly required

MANDATORY STRUCTURE:
- You MUST define a function named main()
- You MUST define a function named __ai_test__()

TEST FUNCTION RULES:
- __ai_test__() MUST call main()
- __ai_test__() MUST return the string "OK" if successful
- If an error occurs, catch it and return e.toString()

CODE QUALITY:
- Keep code minimal
- Use simple logic
- Avoid unnecessary refactoring
- Prefer clarity over cleverness

If you violate ANY rule, the output is considered invalid.
"""

def _extract_text(resp: Message) -> str:
    """
    Claude 응답에서 모든 text block을 안전하게 추출
    """
    if not hasattr(resp, "content") or not resp.content:
        raise RuntimeError("Claude response has no content")

    texts = []

    for block in resp.content:
        if hasattr(block, "type") and block.type == "text" and hasattr(block, "text"):
            texts.append(block.text)
        elif isinstance(block, dict) and block.get("type") == "text":
            texts.append(block.get("text", ""))

    if not texts:
        raise RuntimeError(f"No text block found in Claude response: {resp.content}")

    return "\n".join(texts)


def generate_code(spec: str) -> str:
    """
    Google Apps Script 코드 생성
    """
    user_prompt = f"""
Generate a complete Google Apps Script that fulfills the following requirement.

REQUIREMENT:
{spec}

Remember:
- main() is the entry point
- __ai_test__() must exist and be executable
- Output code only
"""

    resp = client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return _extract_text(resp)


def fix_code(payload: str) -> str:
    return generate_code(payload)
