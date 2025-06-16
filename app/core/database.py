from pathlib import Path
import jaydebeapi

# Ruta al ojdbc11 dentro de la carpeta lib
DRIVER_PATH = str(Path(__file__).parent.parent.parent / "lib" / "ojdbc11.jar")

DATABASE_URL = "jdbc:oracle:thin:@//192.168.112.46:1521/db01"
USERNAME = "data_usr"
PASSWORD = "dataicep1"

def get_connection():
    return jaydebeapi.connect(
        "oracle.jdbc.OracleDriver",
        DATABASE_URL,
        [USERNAME, PASSWORD],
        DRIVER_PATH
    )
