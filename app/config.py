from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings"""
    DATABASE_URL: str = "postgresql://postgres:password@db:5432/urlshortener"
    BASE_URL: str = "http://localhost:8000" 
    SHORT_URL_LENGTH: int = 6 
    PORT: int = 8000  
    HOST: str = "0.0.0.0"  

    @property
    def full_base_url(self) -> str:
        """Get the full base URL including protocol, host and port"""
        return f"http://{self.HOST}:{self.PORT}"

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()
def get_settings():
    """Get cached settings"""
    return Settings()
