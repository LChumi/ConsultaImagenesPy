from fastapi import FastAPI
from app.routers import producto
from app.core import events, config

app = FastAPI(
    title=config.settings.PROJECT_NAME,
    version=config.settings.API_VERSION,
)

app.include_router(producto.router)

@app.on_event("startup")
async def startup():
    await events.startup()

@app.on_event("shutdown")
async def shutdown():
    await events.shutdown()

@app.get("/")
async def root():
    return {"message": "✅ API Lista"}
