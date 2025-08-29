from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16 Pro Max", "+79878543267"),
    Smartphone("Samsung", "Galaxy S23", "+79634674195"),
    Smartphone("Redme", "Redmi 7S", "+79642406260"),
    Smartphone("Huawei", "P50 Pro", "+79068946261"),
    Smartphone("Google", "Pixel 7 Pro", "+7951775894")
]

for item in catalog:
    print(f"{item.brand} - {item.model}. Номер телефона: {item.phone_number}")
