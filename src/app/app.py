from src.message.order.message import OrderStatusMessage
from src.message.order.statuses import AcceptedOperator
from src.app.schemas.order import OrderSchema

import asyncio

o = {
  "client": "Косов Сергей Владимирович",
  "number": "00НФ-013523",
  "date": "2024-12-01T00:00:00",
  "status": "Принят оператором",
  "amount": 10,
  "pay_link": "https://securepayments.tinkoff.ru/4J0Ek30r",
  "pay_status": "NEW",
  "cooking_time_from": "0001-01-01T00:00:00",
  "cooking_time_to": "0001-01-01T13:30:00",
  "delivery_time_from": "0001-01-01T15:00:00",
  "delivery_time_to": "0001-01-01T15:30:00",
  "project": "Дисконт Суши",
  "trade_point": "Московский тракт, 87к1",
  "trade_point_card": "MockoBcku'u TpakT 87 k.1 https://go.2gis.com/pdacd",
  "delivery_method": "Курьер",
  "delivery_adress": "625001, Тюменская обл, г.о. город Тюмень, г Тюмень, ул Полевая, д. 117, к. 2, кв. 145, подъезд 1, этаж 1",
  "phones": ["9829764729"]
}
schema = OrderSchema(**o)
print(schema)

a = AcceptedOperator(order=schema)
print(asyncio.run(OrderStatusMessage().message(status=a)).text)
