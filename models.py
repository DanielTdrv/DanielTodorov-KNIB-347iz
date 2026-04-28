class Car:
    def __init__(self, brand, model, price, country):
        self.brand = brand
        self.model = model
        self.price = price
        self.country = country

    def display_info(self):
        return f"{self.brand} {self.model} - {self.price} €."

    def is_expensive(self):
        return self.price > 25000

    def get_country(self):
        return self.country

# Даниел Тодоров КНИБ - 347iz