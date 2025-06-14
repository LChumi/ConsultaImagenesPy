from fastapi import APIRouter
from app.models.producto import Producto
from app.controllers.producto_controller import (get_all_productos,
                                                  get_producto_by_id)


router = APIRouter(prefix="/producto", tags=["producto"])

@router.get("/id/{pro_codigo}/{pro_empresa}", response_model=Producto)
async def get_producto(pro_codigo: int, pro_empresa: int):
    """
    Get a product by its code and company ID.
    """
    producto = await get_producto_by_id(pro_codigo, pro_empresa)
    if not producto:
        return {"error": "Producto not found"}
    return producto