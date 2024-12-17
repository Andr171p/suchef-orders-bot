import asyncio

from src.app.app import start_aiogram_bot
from src.broadcast.app import start_broadcast


async def main() -> None:
    await asyncio.gather(
        start_aiogram_bot(),
        start_broadcast()
    )


if __name__ == "__main__":
    asyncio.run(main())
