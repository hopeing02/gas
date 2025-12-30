import os
from anthropic import Anthropic

client = Anthropic(api_key=os.environ["CLAUDE_API_KEY"])

SYSTEM_PROMPT = """
You are a Google Apps Script expert.
Do not modify triggers, scopes, or permissions.
Only fix function bodies.
"""

def generate_code(spec):
    return client..messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": str(spec)}]
        thinking={"type": "enabled", "budget_tokens": 2000}
    ).content[0].text

def fix_code(payload):
    return generate_code(payload)