import os
from dotenv import load_dotenv
from app.services.image_processor import image_processor
from app.core.database import get_connection
from app.models.producto import Producto

load_dotenv()

IMAGES_DIR = os.getenv("IMAGES_DIR", "images")

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

def buscar_similares(features_uploaded, top_n=3):
    resultados = []
    for filename in os.listdir(IMAGES_DIR):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')):
            continue
        img_path = os.path.join(IMAGES_DIR, filename)
        features_candidate = image_processor.extract_features(img_path)
        if features_candidate is None:
            continue
        score = image_processor.calculate_similarity(features_uploaded, features_candidate)
        resultados.append((filename, score))
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados[:top_n]

def get_productos_by_pro_id(pro_empresa: int, pro_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT PRO_EMPRESA, PRO_CODIGO, PRO_ID, PRO_NOMBRE FROM PRODUCTO WHERE PRO_ID = ? AND PRO_EMPRESA = ?",
        [pro_id, pro_empresa]
    )
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return Producto.from_tuple(row) if row else None

