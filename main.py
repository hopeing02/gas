from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from api import generate, test, fix, deploy

app = FastAPI(title="GAS AI Platform")

# 🔹 정적 파일 (CSS, JS)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# 🔹 API
app.include_router(generate.router, prefix="/api")
app.include_router(test.router, prefix="/api")
app.include_router(fix.router, prefix="/api")
app.include_router(deploy.router, prefix="/api")

# 🔥 루트에서 index.html 반환 (이게 핵심)
@app.get("/")
def root():
    return FileResponse("frontend/index.html")
