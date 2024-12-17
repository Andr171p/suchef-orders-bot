from src.broadcast.callback import on_message
from src.broadcast.rmq import consumer


async def start_broadcast() -> None:
    await consumer.consume(on_message)
