from aiogram.types.base import MutableTelegramObject

from src.message import utils
from src.message.base import BasePath
from src.app.schemas.order import OrderSchema
from src.app.keyboards.order_status import pay_link_kb, confirmed_link_kb


class OrderStatus(BasePath):

    def __init__(self, order: OrderSchema) -> None:
        self.order = order

    async def photo(self) -> bytes:
        return await utils.load_png(self.photo_path)

    async def text(self) -> str:
        template: str = await utils.load_txt(self.text_path)
        return template.format(**self.order.model_dump())

    async def keyboard(self) -> MutableTelegramObject:
        pay_link: str = self.order.pay_link
        if self.order.pay_status != "CONFIRMED":
            return await pay_link_kb(url=pay_link)
        return await confirmed_link_kb(url=pay_link)
