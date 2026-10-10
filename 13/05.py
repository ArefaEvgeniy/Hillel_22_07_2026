class Dog:
    tail = True
    legs = 4

    def say(self):
        print("Woof!")

    def go(self):
        print("I am going for a walk.")

    def bark(self):
        print("Woof! Woof!")


class Cat(Dog):

    def say(self):
        print("Meow!")


cat_1 = Cat()
cat_1.go()
print(cat_1.legs)
cat_1.say()
cat_1.bark()
