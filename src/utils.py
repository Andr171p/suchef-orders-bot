import re
import json
import aiofiles
from pathlib import Path
from typing import Dict


async def load_json(path: Path | str) -> Dict[str, str]:
    async with aiofiles.open(
        file=path,
        mode='r',
        encoding='utf-8'
    ) as file:
        data = await file.read()
        return json.loads(data)


async def load_txt(path: Path | str) -> str:
    async with aiofiles.open(
        file=path,
        mode='r',
        encoding='utf-8'
    ) as file:
        return await file.read()


def is_phone_format(phone: str) -> bool:
    pattern = r'\+\d$\d{3}$\d{3}-\d{2}-\d{2}'
    return bool(re.fullmatch(pattern, phone))
