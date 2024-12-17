from aio_pika import IncomingMessage
from typing import Dict

from src.broadcast.send import send_message
from src.broadcast.logger import logger


async def on_message(message: IncomingMessage) -> None:
    async with message.process():
        body: str = message.body.decode("utf-8")
        headers: Dict[str, str] = message.headers
        logger.info(f"[x] Received: [{body}]")
        await send_message(
            body=body,
            headers=headers
        )
