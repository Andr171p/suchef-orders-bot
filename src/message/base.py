from pathlib import Path
from aiogram.types.base import MutableTelegramObject
from aiogram.types.input_file import InputFile


class BaseTextMessage:
    text: str
    keyboard: MutableTelegramObject | None


class BasePhotoMessage:
    photo: InputFile
    text: str
    keyboard: MutableTelegramObject | None


class BasePath:
    photo_path: Path | str = None
    text_path: Path | str = None
