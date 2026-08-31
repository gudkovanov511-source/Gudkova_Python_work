class Smartphone:
    # phone_number ожидается в формате "+79..."
    def __init__(self, brand, model, phone_number: str):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number
