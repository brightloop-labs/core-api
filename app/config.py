from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://core:core@localhost:5432/core"
    jwt_secret: str = "change-me"

    class Config:
        env_file = ".env"


settings = Settings()