my_list = ["rr", 2, -66, 88, -5, "45", "Hello", -100, 0, -8]

indexes = []
for index, value in enumerate(my_list):
    if isinstance(value, (int, float)) and value < 0:
    # if type(item[1]) == int and item[1] < 0:
        indexes.append(index)

print("-----")
print("Индексы отрицательных чисел в списке:", indexes)
