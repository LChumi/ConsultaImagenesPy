from app.database import db
from app.models.producto import Producto

async def get_all_productos():
    productos = []
    for doc in db.producto.find():
        producto = Producto(**doc)
        productos.append(producto)
    return productos

async def get_producto_by_id(pro_codigo: int, pro_empresa: int):
    doc = db.producto.find_one({"PRO_CODIGO": pro_codigo, "PRO_EMPRESA": pro_empresa})
    if doc:
        return Producto(**doc)
    return None