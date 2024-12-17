from dataclasses import dataclass

from src.message.order.base import OrderStatus
from src.message.order import statuses
from src.app.schemas.order import OrderSchema


@dataclass
class Status:
    order: OrderSchema

    def get_order_status(self) -> OrderStatus:
        status: str = self.order.status
        match status:
            case "Принят оператором":
                return statuses.AcceptedOperator(self.order)
            case "Передан на кухню":
                return statuses.TransferredToKitchen(self.order)
            case "Готовится":
                return statuses.Cooking(self.order)
            case "Приготовлен":
                return statuses.Cooked(self.order)
            case "Укомплектован":
                return statuses.Staffed(self.order)
            case "Передан курьеру":
                return statuses.TransferredToCourier(self.order)
            case "Доставлен":
                return statuses.Delivered(self.order)
            case "Готов для выдачи":
                return statuses.ReadyForPickup(self.order)
            case "Завершен":
                return statuses.CompletedSuccessfully(self.order)
            case "Отменен":
                return statuses.Canceled(self.order)
