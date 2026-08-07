my_list = [2, -10, 55, 778, 46, -100]

new_list = [item ** 2 for item in my_list]

new_list_2 = ["RR" for item in my_list]

new_list_3 = [item * 2 for item in my_list if item > 0]

print("Новый список:", new_list)
print("Новый список 2:", new_list_2)
print("Новый список 3:", new_list_3)
