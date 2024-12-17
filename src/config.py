import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class DBSettings(BaseSettings):
    user: str = os.getenv("DB_USER")
    password: str = os.getenv("DB_PASSWORD")
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")
    database: str = os.getenv("DB_DATABASE")

    url: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"
    echo: bool = True


class APISettings(BaseSettings):
    url: str = os.getenv("API_URL")
    headers: Dict[str, str] = {"Content-Type": "application/json; charset=UTF-8"}


class MessagesSettings(BaseSettings):
    statuses: Path = BASE_DIR / "src" / "app" / "statics" / "text" / "statuses"
    images: Path = BASE_DIR / "src" / "app" / "statics" / "images" / "statuses"


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    api: APISettings = APISettings()
    msg: MessagesSettings = MessagesSettings()


settings = Settings()
