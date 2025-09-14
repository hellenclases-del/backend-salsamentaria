from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "root"
    DB_PASSWORD: str = "hvalles2008"  # coloca tu clave real aquí
    DB_HOST: str = "localhost"
    DB_PORT: str = "3306"
    DB_NAME: str = "salsamentaria"

    @property
    def DATABASE_URL(self):
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()