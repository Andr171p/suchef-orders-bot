import aiohttp
from typing import Any, Dict

from src.app.schemas.utils import format_phone
from src.utils import is_phone_format
from src.api.logger import logger
from src.config import settings


def is_ok(response: aiohttp.ClientResponse) -> bool:
    return True if response.status == 200 else False


async def get_user_orders(phone: str) -> Dict[str, Any]:
    if not is_phone_format(phone):
        phone = format_phone(phone)
    data: Dict[str, str] = {
        "command": "status",
        "telefon": phone
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=settings.api.url,
                headers=settings.api.headers,
                json=data
            ) as response:
                if is_ok(response=response):
                    return await response.json()
    except aiohttp.client_exceptions.ClientConnectorError as _ex:
        logger.critical(_ex)
