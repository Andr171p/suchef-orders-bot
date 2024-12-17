import logging

from src.app.bot import bot, dp


async def start_aiogram_bot() -> None:
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
