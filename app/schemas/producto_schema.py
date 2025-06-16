from pydantic import BaseModel

class ProductoResponse(BaseModel):
    PRO_EMPRESA: int
    PRO_CODIGO: int
    PRO_ID: str
    PRO_NOMBRE: str
