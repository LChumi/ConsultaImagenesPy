from app.database import engine
from sqlalchemy.ext.asyncio import AsyncEngine

#Si se usa SQLAlchemy async, cierra el engine async 
async def shutdown():
    if isinstance(engine, AsyncEngine):
        await engine.dispose()
    else:
        # sync engine 
        engine.dispose()
        
# Si quieres acciones al arrancar:
async def startup():
    # Ejemplo: ping a la base de datos
    print("App starting up...")