data = [0, 1, 2, 3, 4, 5]


def fn(x):
    return x % 2 != 0


new_data2 = list(filter(fn, data))
print(new_data2)


new_data3 = list(filter(lambda x: x % 2 != 0, data))
print(new_data3)
