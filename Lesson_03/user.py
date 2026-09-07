class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayFirstName(self):
        print(f"Меня зовут {self.first_name}")

    def sayLastName(self):
        print(f"Моя фамилия {self.last_name}")

    def sayFullName(self):
        print(f"Моё полное имя {self.first_name} {self.last_name}")
