import subprocess

def run_test():
    out = subprocess.check_output([
        "clasp", "run", "__ai_test__"
    ])
    return {"log": out.decode()}
