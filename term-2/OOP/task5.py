from datetime import date

class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def get_age(self) -> int:
        return date.today().year - self.year

car = Car("Toyota", "Camry", 2015)
print(car.get_age())