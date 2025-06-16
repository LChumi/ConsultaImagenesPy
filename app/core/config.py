from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # Oracle
    ORACLE_USER: str = Field(default="data_usr")
    ORACLE_PASSWORD: str = Field(default="dataicep1")
    ORACLE_HOST: str = Field(default="192.168.112.46")
    ORACLE_PORT: int = Field(default=1521)
    ORACLE_SERVICE_NAME: str = Field(default="db01")

    @property
    def ORACLE_URI(self) -> str:
        return (
            f"oracle+oracledb://{self.ORACLE_USER}:{self.ORACLE_PASSWORD}"
            f"@{self.ORACLE_HOST}:{self.ORACLE_PORT}/?service_name={self.ORACLE_SERVICE_NAME}"
        )

    # Otros settings escalables:
    API_VERSION: str = "1.0.0"
    PROJECT_NAME: str = "API Consulta Productos por Imágenes"

    class Config:
        env_file = ".env"

settings = Settings()
