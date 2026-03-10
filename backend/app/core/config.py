from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Legal Analyzer"
    debug: bool = True

    mongo_url: str
    redis_url: str

    class Config:
        env_file = ".env"


settings = Settings()