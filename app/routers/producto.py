from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.producto_schema import ProductoResponse
from app.services.producto_service import get_producto, get_productos_by_pro_id

router = APIRouter(prefix="/productos", tags=["productos"])

# ✅ Primero la específica
@router.get("/by_pro_id/{pro_id}", response_model=List[ProductoResponse])
def listar_productos_por_pro_id(pro_id: str):
    productos = get_productos_by_pro_id(pro_id)
    return [p.__dict__ for p in productos]

# ✅ Luego la genérica
@router.get("/{pro_empresa}/{pro_codigo}", response_model=ProductoResponse)
def obtener_producto(pro_empresa: int, pro_codigo: int):
    producto = get_producto(pro_empresa, pro_codigo)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto.__dict__

