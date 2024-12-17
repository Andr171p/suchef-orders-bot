from pathlib import Path
from aiogram.types.base import MutableTelegramObject


class BaseTextMessage:
    chat_id: int | None
    text: str
    keyboard: MutableTelegramObject | None


class BasePhotoMessage:
    chat_id: int | None
    photo: bytes
    text: str
    keyboard: MutableTelegramObject | None


class BasePath:
    photo_path: Path | str = None
    text_path: Path | str = None
