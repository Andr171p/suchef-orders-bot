from pathlib import Path
from typing import Dict, Any, Self
from dataclasses import dataclass

from src.config import settings
from src.messages.base import BaseMessage, BaseStatus


statuses_dir: Path = settings.msg.statuses

images_dir: Path = settings.msg.images


class New(BaseStatus):
    pass


class AcceptedOperatorCourier(BaseStatus):
    path: Path = statuses_dir / "Принят оператором Курьер.txt"

    async def message(self) -> BaseMessage:
        text = await self.status(self.path)
        reply_markup = await self.keyboard()
        return BaseMessage(
            text=text,
            reply_markup=reply_markup
        )