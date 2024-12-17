from pathlib import Path

from src.config import settings
from src.message import utils
from src.message.order.base import OrderStatus


text_dir: Path = settings.msg.statuses

photo_dir: Path = settings.msg.images


class New:
    pass


class AcceptedOperator(OrderStatus):
    photo_path: Path = photo_dir / "2_Принят оператором.png"

    async def text(self) -> str:
        if self.order.delivery_method != "Курьер":
            path: Path = text_dir / "Принят оператором Самовывоз.txt"
            template: str = await utils.load_txt(path)
            return template.format(**self.order.model_dump())
        path: Path = text_dir / "Принят оператором Курьер.txt"
        template: str = await utils.load_txt(path)
        return template.format(**self.order.model_dump())


class TransferredToKitchen(OrderStatus):
    photo_path: Path = photo_dir / "3_Передан на кухню.png"
    text_path: Path = text_dir / "Передан на кухню.txt"


class Cooking(OrderStatus):
    photo_path: Path = photo_dir / "4_Готовится.png"
    text_path: Path = text_dir / "Готовится.txt"


class Cooked(OrderStatus):
    photo_path: Path = photo_dir / "5_Приготовлен.png"
    text_path: Path = text_dir / "Приготовлен.txt"


class Staffed(OrderStatus):
    photo_path: Path = photo_dir / "6_Укомплектован.png"
    text_path: Path = text_dir / "Укомплектован.txt"


class TransferredToCourier(OrderStatus):
    photo_path: Path = photo_dir / "7_Передан курьеру.png"
    text_path: Path = text_dir / "Передан курьеру.txt"


class ReadyForPickup(OrderStatus):
    photo_path: Path = photo_dir / "8_Готов к выдаче.png"
    text_path: Path = text_dir / "Готов для выдачи.txt"


class Delivered(OrderStatus):
    photo_path: Path = photo_dir / "9_Доставлен.png"
    text_path: Path = text_dir / "Доставлен.txt"


class CompletedSuccessfully(OrderStatus):
    photo_path: Path = photo_dir / "10_Завершен успешно.png"
    text_path: Path = text_dir / "Завершен.txt"


class Canceled(OrderStatus):
    photo_path: Path = photo_dir / "11_Отменен.png"
    text_path: Path = text_dir / "Отменен.txt"
