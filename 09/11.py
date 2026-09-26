def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
for value in my_generator():
    print(value)
