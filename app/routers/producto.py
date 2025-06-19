from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List
from app.schemas.producto_schema import ProductoResponse
from app.services.producto_service import get_producto, get_productos_by_pro_id, buscar_similares
from app.services.image_processor import image_processor
import os

router = APIRouter(prefix="/productos", tags=["productos"])

# Específica
@router.get("/by_pro_id/{pro_id}/empresa/{empresa}", response_model=List[ProductoResponse])
def listar_productos_por_pro_id(pro_id: str, empresa: int):
    productos = get_productos_by_pro_id(empresa, pro_id)
    return [p.__dict__ for p in productos] if productos else []

# Genérica
@router.get("/{pro_empresa}/{pro_codigo}", response_model=ProductoResponse)
def obtener_producto(pro_empresa: int, pro_codigo: int):
    producto = get_producto(pro_empresa, pro_codigo)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto.__dict__

@router.post("comparar-imagen")
async def comparar_imagen(file: UploadFile = File(...)):
    """
    Compara una imagen cargada con las imágenes almacenadas y devuelve los productos similares.
    """
    file_bytes = await file.read()
    features_uploaded = image_processor.extract_features_from_bytes(file_bytes)
    
    if features_uploaded is None:
        return {"error": "No se pudieron extraer características de la imagen cargada."}
    
    top_matches = buscar_similares(features_uploaded, top_n=3)
    
    productos = []
    for filename, score in top_matches:
        try:
            barra, _ = os.path.splitext(filename)
            producto = get_productos_by_pro_id(2, barra)
            productos.append({
                "archivo": filename,
                "similaridad": score,
                "producto": producto.__dict__ if producto else None
            })
        except Exception as e:
            productos.append({
                "archivo": filename,
                "similaridad": score,
                "error": str(e)
            })
    return {"coincidencias": productos}