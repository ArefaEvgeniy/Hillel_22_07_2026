data = [1, 2, 3, 4, 5]

new_data = []
for i in data:
    new_data.append(i ** 3)
print(new_data)


def fn(x):
    return x ** 3


new_data2 = list(map(fn, data))
print(new_data2)


new_data3 = list(map(lambda x: x ** 3, data))
print(new_data3)
