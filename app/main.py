from fastapi import FastAPI
from app.routers import producto
from app.core import events

app = FastAPI(
    title="API Consulta Productos por Imagenes",
    version="1.0.0",
)

#Routers
app.include_router(producto.router)


#Eventos de arranque 
@app.on_event("startup")
async def startup():
    await events.startup()

@app.on_event("shutdown")
async def shutdown():
    await events.shutdown()

@app.get("/")
async def root():
    return {"message": "API Consulta Productos por Imagenes inicializado"}