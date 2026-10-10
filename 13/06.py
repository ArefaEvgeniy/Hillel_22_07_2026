class Animal:
    tail = True
    legs = 4

    def go(self):
        print("I am going for a walk.")


class Dog(Animal):

    def say(self):
        print("Woof!")

    def bark(self):
        print("Woof! Woof!")


class Cat(Animal):

    def say(self):
        print("Meow!")


cat_1 = Cat()
cat_1.go()
print(cat_1.legs)
cat_1.say()
