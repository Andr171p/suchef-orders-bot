from typing import Dict, Optional

from src.database.service import user_service
from src.broadcast.order_status import send_order_status
from src.app.schemas.order import OrderSchema


async def send_message(
        body: str,
        headers: Dict[str, str]
) -> None:
    order = OrderSchema.parse_raw(body)
    if headers['project'] != "Дисконт Суши":
        for phone in order.phones:
            user = await user_service.get_user(phone)
            user_id: Optional[int] = user.user_id if user is not None else None
            await send_order_status(
                user_id=user_id,
                order=order
            )
