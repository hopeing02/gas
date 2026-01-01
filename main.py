from fastapi import FastAPI
from api import generate, test, fix, deploy
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="gas ai platform")

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def root():
    return FileResponse("frontend/index.html")

app.include_router(generate.router)
app.include_router(test.router)
app.include_router(fix.router)
app.include_router(deploy.router)