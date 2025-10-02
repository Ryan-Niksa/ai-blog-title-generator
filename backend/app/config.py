from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str | None = None
    DATABASE_URL: str = "sqlite:///./blog.db"

    class Config:
        env_file = ".env"

settings = Settings()
