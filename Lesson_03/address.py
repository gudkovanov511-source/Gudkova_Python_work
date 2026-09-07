class Address:
    def __init__(
            self, index: str, city: str, street: str, house: str,
            flat: str
                  ):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def full_adress(self):
        return (
            f"{self.index}, {self.city}, {self.street}, {self.house}"
            f" - {self.flat}"
               )
