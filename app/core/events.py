from app.core.database import get_connection

async def startup():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM dual")
        result = cursor.fetchone()
        print("Conexión a la base de datos exitosa:", result)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Conexión a la base de datos fallida:", e)

async def shutdown():
    print("App apagándose...")
    # No hace falta cerrar nada global porque no tienes `db` singleton
