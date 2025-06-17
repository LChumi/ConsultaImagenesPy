import os
from app.services.image_processor import ImageProcessor
from app.core.database import get_connection
from app.models.producto import Producto

IMAGES_DIR = "IMAGES"

def get_producto(pro_empresa: int, pro_codigo: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT PRO_EMPRESA, PRO_CODIGO, PRO_ID, PRO_NOMBRE FROM PRODUCTO WHERE PRO_EMPRESA = ? AND PRO_CODIGO = ?",
        [pro_empresa, pro_codigo]
    )
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return Producto.from_tuple(row) if row else None

def get_productos_by_pro_id(pro_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT PRO_EMPRESA, PRO_CODIGO, PRO_ID, PRO_NOMBRE FROM PRODUCTO WHERE PRO_ID = ?",
        [pro_id]
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Producto.from_tuple(row) for row in rows]
