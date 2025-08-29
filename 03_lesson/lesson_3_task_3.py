from mailing import Mailing
from address import Address

to_addr = Address(
    index="454084",
    city="Челябинск",
    street="Калинина",
    house="5",
    apartment="39"
)

from_addr = Address(
    index="628394",
    city="Москва",
    street="Тверская",
    house="35",
    apartment="8"
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track="TRACK-555777"
)

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house}-{mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street},  {mailing.to_address.house}-{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
