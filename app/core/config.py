from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # NOTE: .envファイルや環境変数が同名の変数にセットされる
    TITLE: str = "FastAPI App"
    ENV: str = ""
    DEBUG: bool = False
    VERSION: str = "0.0.1"
    CORS_ORIGINS: list[str] = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://localhost:3333",
    ]
    BASE_DIR_PATH: str = str(Path(__file__).parent.parent.absolute())
    ROOT_DIR_PATH: str = str(Path(__file__).parent.parent.parent.absolute())
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str = "secret"

    class Config:
        env_file = ".env"
        extra = "allow"  # this allows environment variables only present in .env file in local development.


def get_settings() -> Settings:
    return Settings()
