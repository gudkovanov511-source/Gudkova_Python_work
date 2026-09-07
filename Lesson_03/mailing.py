from address import Address


class Mailing:
    def __init__(
            self, to_address: Address, from_address: Address,
            const: float, track: str
            ):
        self.to_address = to_address
        self.from_address = from_address
        self.const = const
        self.track = track

    def full_way(self):
        return (
            f"Отправление {self.track} из {self.from_address.full_adress()} "
            f"в {self.to_address.full_adress()}. Стоимость {self.const} "
            f"рублей."
        )
