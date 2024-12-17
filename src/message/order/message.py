from src.message.base import BasePhotoMessage
from src.message.order.base import OrderStatus


class OrderStatusMessage(BasePhotoMessage):
    async def message(self, status: OrderStatus) -> "BasePhotoMessage":
        self.photo = await status.photo()
        self.text = await status.text()
        self.keyboard = await status.keyboard()
        return self
