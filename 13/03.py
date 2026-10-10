class Car:
    def __init__(self, year=None, make=None, model=None):
        self.year = year
        self.make = make
        self.model = model

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


car_1 = Car(2020, "Toyota", "Camry")
car_2 = Car(2021, "Honda", "Civic")
car_3 = Car()

print(car_1.year)
print(car_1.get_info())
print(car_2.get_info())
print(car_3.get_info())
