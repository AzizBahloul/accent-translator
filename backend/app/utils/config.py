from pydantic import BaseSettings

class Config(BaseSettings):
    APP_NAME: str = "Accent Translator"
    VERSION: str = "1.0.0"
    LOG_LEVEL: str = "DEBUG"
    ALLOWED_ORIGINS: list[str] = ["*"]

    class Config:
        env_file = ".env"

config = Config()
