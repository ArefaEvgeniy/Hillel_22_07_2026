class Woman:
    def __init__(self, name, age, weight=None):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        if self.__weight < 45:
            return round(self.__weight * 1.1, 2)
        elif self.__weight > 60:
            return round(self.__weight * 0.75, 2)
        else:
            return self.__weight


obj = Woman("Alice", 30, 90)
print(obj.name)  # Output: Alice
print(obj._age)  # Output: 30
print(obj._Woman__weight)  # Output: 60 (accessing private attribute using name mangling)
print(obj.get_weight())
