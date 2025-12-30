from fastapi import FastAPI
from api import generate, test, fix, deploy
app = FastAPI(title="gas ai platform")
app.include_router(generate.router)
app.include_router(test.router)
app.include_router(fix.router)
app.include_router(deploy.router)