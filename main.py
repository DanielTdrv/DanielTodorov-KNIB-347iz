from models import Car

cars = [
    Car("BMW", "X7", 40000, "Германия"),
    Car("Audi", "S4", 20000, "Германия"),
    Car("Mercedes", "C-Class W223", 30000, "Германия"),
    Car("Volkswagen", "Golf 7", 18000, "Германия"),

    Car("Toyota", "Corolla", 15000, "Япония"),
    Car("Honda", "Civic", 19000, "Япония"),
    Car("Subaru", "WRX", 18000, "Япония"),
    Car("Mazda", "RX7", 23000, "Япония"),

    Car("Ferrari", "812 Superfast", 250000, "Италия"),
    Car("Lamborghini", "Huracan Evo", 300000, "Италия"),
    Car("Fiat", "500", 5000, "Италия"),
    Car("Alfa Romeo", "Giulia", 55000, "Италия")
]
countries = ["Германия", "Япония", "Италия"]

print("\n\033[1mЗдравейте,\nДобре дошли в автосалона на Даниел Тодоров!\033[m")
for country in countries:
    print("\n===")
    print(f"- \033[1m{country} автомобили\033[m")
    print("===")

    print("\nЕвтини автомобили (под 25000 €):")
    for car in cars:
        if car.get_country() == country and not car.is_expensive():
            print(" - " + car.display_info())

    print("\nСкъпи автомобили (над 25000 €):")
    for car in cars:
        if car.get_country() == country and car.is_expensive():
            print(" - " + car.display_info())


print("\n===")
print("\033[1mНай-скъпа кола от всяка държава\033[m")
most_expensive_car = None
print("===")

for country in countries:
    most_expensive_car = None

    for car in cars:
        if car.get_country() == country:
            if most_expensive_car is None or car.price > most_expensive_car.price:
                most_expensive_car = car

    print(f"\n{country}:")
    print(" - " + most_expensive_car.display_info())

    # Даниел Тодоров КНИБ - 347iz