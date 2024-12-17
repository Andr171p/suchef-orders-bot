import json
import aiofiles
from pathlib import Path
from typing import Dict, Any


async def load_json(path: Path | str) -> Dict[str, Any]:
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


async def load_png(path: Path | str) -> bytes:
    async with aiofiles.open(
        file=path,
        mode='rb'
    ) as file:
        return await file.read()
