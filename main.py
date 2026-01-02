from fastapi import FastAPI
from api import generate, test, fix, deploy
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="gas ai platform")

app.mount("/static", StaticFiles(directory="frontend/static",html=True), name="static") 
app.include_router(generate.router, prefix="/api")
app.include_router(test.router,prefix="/api")
app.include_router(fix.router,prefix="/api")
app.include_router(deploy.router,prefix="/api")
