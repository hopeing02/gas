from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from api import generate, fix, test, deploy

app = FastAPI(title="GAS AI Platform")

# frontend 정적 파일
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# API는 /api prefix로 통일
app.include_router(generate.router, prefix="/api")
app.include_router(fix.router, prefix="/api")
app.include_router(test.router, prefix="/api")
app.include_router(deploy.router, prefix="/api")

# index.html 서빙
@app.get("/")
def root():
    return FileResponse("frontend/index.html")
