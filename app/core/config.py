from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Pulse Engine"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "7df61a84f3e6a98d3618451b6e4d412e8b61c56910243b6ef943e86c12d4a159"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 # 24 hours
    DATABASE_URL: str = "sqlite+aiosqlite:///./pulse.db"

    class Config:
        case_sensitive = True

settings = Settings()
