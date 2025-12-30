FORBIDDEN = [
    "ScriptApp.newTrigger",
    "DriveApp.remove",
    "UrlFetchApp.fetch("
]

def validate(code: str) -> bool:
    return not any(x in code for x in FORBIDDEN)