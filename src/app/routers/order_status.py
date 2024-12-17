from aiogram import F, Router
from aiogram.types import Message
from typing import Any, Dict, List


from src.app.schemas.order import OrderSchema
from src.message.order.status import Status
from src.message.order.message import OrderStatusMessage
from src.database.service import user_service
from src.api import service as api_service
from src.utils import load_json
from src.config import settings


status_router = Router()


@status_router.message(F.text == "Статус заказа")
async def get_order_status(message: Message) -> None:
    user_id: int = message.from_user.id
    user = await user_service.get_user(user_id)
    phone: str = user.phone
    response: Dict[str, Any] = await api_service.get_user_orders(phone)
    orders: List[Dict[str, Any]] = response['data']['orders']
    if len(orders) != 0:
        for order in orders:
            if order['project'] != "Дисконт Суши":
                status = Status(OrderSchema(**order)).get_order_status()
                bot_message = await OrderStatusMessage().message(status)
                await message.answer(
                    text=bot_message.text,
                    reply_markup=bot_message.keyboard
                )
    else:
        template: Dict[str, str] = await load_json(path=settings.msg.auth)
        await message.answer(
            text=template['empty']
        )
