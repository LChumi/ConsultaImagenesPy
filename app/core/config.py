from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Oracle
    ORACLE_USER: str
    ORACLE_PASSWORD: str
    ORACLE_HOST: str
    ORACLE_PORT: int
    ORACLE_SERVICE_NAME: str

    # Directorio de imágenes
    IMAGES_DIR: str

    # Propiedad para construir el DSN o URI
    @property
    def ORACLE_URI(self) -> str:
        return (
            f"oracle+oracledb://{self.ORACLE_USER}:{self.ORACLE_PASSWORD}"
            f"@{self.ORACLE_HOST}:{self.ORACLE_PORT}/?service_name={self.ORACLE_SERVICE_NAME}"
        )

    # Otros settings opcionales
    API_VERSION: str = "1.0.0"
    PROJECT_NAME: str = "API Consulta Productos por Imágenes"

    class Config:
        env_file = ".env"


settings = Settings()
