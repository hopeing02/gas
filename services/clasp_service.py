import subprocess

def deploy():
    subprocess.check_call(["clasp", "push"])
    out = subprocess.check_output(["clasp", "deploy"])
    return {"result": out.decode()}