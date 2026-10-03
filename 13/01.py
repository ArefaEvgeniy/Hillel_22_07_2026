class Dog:
    tail = True
    legs = 4

    def bark(self):
        print("Woof!")

    def say(self):
        print("I am a dog.")

    def go(self):
        print("I am going for a walk.")


obj_1 = Dog()
obj_1.go()
obj_1.bark()
print(obj_1.legs)

obj_2 = Dog()
obj_2.name = "Buddy"
obj_2.legs = 3

print(obj_2.name)
print(obj_2.legs)

obj_3 = Dog()

Dog.legs = 5
print(f"Legs of obj_1: {obj_1.legs}")
print(f"Legs of obj_2: {obj_2.legs}")
print(f"Legs of obj_3: {obj_3.legs}")

print(obj_1.__dict__)
print(obj_2.__dict__)
print(obj_3.__dict__)
