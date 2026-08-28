my_list = [55, 3.14, -100, 0, "hello", 0, 3.14, -100, (4, 77, "RR"), 0, "hello", -100, "AA", 0]

new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)

print(list(set(my_list)))
