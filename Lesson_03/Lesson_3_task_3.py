from address import Address
from mailing import Mailing

from_addr = Address(
    "125478", "Москва", "улица Фантастическая", "д. 25", "кв. 71"
    )
to_addr = Address(
    "965874", "Иваново", "улица Небывалая", "д. 32/2", "кв. 5"
)

mail = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    const=145.20,
    track="FDWT123"
    )

print(mail.full_way())
