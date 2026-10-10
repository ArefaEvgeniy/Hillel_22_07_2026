class Car:
    year = None
    make = None
    model = None

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


car_1 = Car()
car_1.year = 2020
car_1.make = "Toyota"
car_1.model = "Camry"

car_2 = Car()
car_2.year = 2021
car_2.make = "Honda"
car_2.model = "Civic"

car_3 = Car()

print(car_1.year)
print(car_1.get_info())
print(car_2.get_info())
print(car_3.get_info())
