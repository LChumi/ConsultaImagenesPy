from typing import List, Optional
from app.models.producto import Producto

def get_productos(db: Session) -> List[Producto]:
    return db.query(Producto).all()

def get_producto(db: Session, pro_empresa: int, pro_codigo: int) -> Optional[Producto]:
    return db.query(Producto).filter(
        Producto.PRO_EMPRESA == pro_empresa,
        Producto.PRO_CODIGO == pro_codigo
    ).first()

def crear_producto(db: Session, producto: Producto) -> Producto:
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto

def eliminar_producto(db: Session, pro_empresa: int, pro_codigo: int) -> bool:
    producto = get_producto(db, pro_empresa, pro_codigo)
    if producto:
        db.delete(producto)
        db.commit()
        return True
    return False
