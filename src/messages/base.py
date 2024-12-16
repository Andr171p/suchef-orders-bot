from pathlib import Path
from pydantic import BaseModel
from typing import Dict, Any
from dataclasses import dataclass
from aiogram.types.base import MutableTelegramObject

from src import utils
from src.app.schemas.order import OrderSchema
from src.app.keyboards.order_status import pay_link_kb, confirmed_link_kb


class BaseMessage(BaseModel):
    text: str
    reply_markup: MutableTelegramObject | None


@dataclass
class BaseStatus:
    order: OrderSchema

    async def status(self, path: Path | str) -> str:
        status_template = await utils.load_txt(path)
        return status_template.format(**self.order.model_dump())

    async def keyboard(self) -> MutableTelegramObject:
        pay_link: str = self.order.pay_link
        if self.order.pay_status != "CONFIRMED":
            return await pay_link_kb(pay_link)
        return await confirmed_link_kb(pay_link)
