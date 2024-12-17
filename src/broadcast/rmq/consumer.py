import asyncio
import aio_pika

from src.config import settings


async def consume(
        callback: callable,
        routing_key: str = settings.rmq.queue_name,
        url: str = settings.rmq.url
) -> None:
    connection = await aio_pika.connect_robust(url)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(routing_key)
        await queue.consume(callback)
        await asyncio.Future()
