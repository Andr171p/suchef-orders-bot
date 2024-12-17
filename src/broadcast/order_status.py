from src.message.order.status import Status
from src.message.order.message import OrderStatusMessage
from src.broadcast.logger import logger
from src.app.schemas.order import OrderSchema
from src.app.bot import bot


async def send_order_status(
        user_id: int,
        order: OrderSchema
) -> None:
    status = Status(order).get_order_status()
    message = await OrderStatusMessage().message(status)
    try:
        await bot.send_photo(
            chat_id=user_id,
            photo=message.photo,
            caption=message.text,
            reply_markup=message.keyboard
        )
        logger.info(f"message sent to user_id=[{user_id}] successfully")
    except Exception as _ex:
        logger.warning(_ex)
        logger.warning(f"message was not sent")
