import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["CLAUDE_API_KEY"])

SYSTEM_PROMPT = """
You are a Google Apps Script expert.
Do not modify triggers, scopes, or permissions.
Only fix function bodies.
<<<<<<< HEAD
=======
You are a senior Python engineer.
Rules:
- Output ONLY valid Python code
- No markdown
- No explanation
- Python 3.13 compatible
- If an error is provided, fix only that error
>>>>>>> 9ccf4c3b5649425d0074fe8304f4021b0bd1c5ba
"""

def generate_code(spec):
    resp = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": str(spec)}
        ],
        thinking={"type": "enabled", "budget_tokens": 2000},
    )
    return resp.content[0].text

def fix_code(payload):
    return generate_code(payload)
