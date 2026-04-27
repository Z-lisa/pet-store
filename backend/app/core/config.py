from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str = "温馨宠物店 API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "宠物店全栈项目后端 API"
    
    # CORS
    BACKEND_CORS_ORIGINS: list = ["*"]
    
    # Database
    DATABASE_URL: str = "sqlite:///./pet_store.db"
    
    # Security
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    
    class Config:
        env_file = ".env"


settings = Settings()
