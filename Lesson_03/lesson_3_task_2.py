from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 17 Pro Max", "+79031254982"),
    Smartphone("Samsung", "Galaxy S26 Ultra", "+79162487913"),
    Smartphone("Xiaomi", "Xiaomi 17 Ultra", "+79254567182"),
    Smartphone("OnePlus", "OnePlus 15", "+79695284859"),
    Smartphone("Google", "Pixel 10 Pro", "+79254182364")
]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. "
          f"{phone.phone_number}"
          )
