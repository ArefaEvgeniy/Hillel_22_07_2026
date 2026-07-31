my_list = [1, 2.23, [0, 99, "RRR"], 100, -44, "Hello", True, 101]

print(-44 in my_list)
print(-43 in my_list)
print(99 in my_list)

print(my_list[5])
# print(my_list[10])
print(my_list[0])
last_element = len(my_list) - 1
print(my_list[last_element])
print(my_list[-1])
print(my_list[3])
print(my_list[-5])

new_list = my_list[3:6]
print(new_list)

print(my_list[3:])
print(my_list[0:])
print(my_list[:])
print(my_list[2:7:3])
print(my_list[5::-2])
print(my_list[-1::-1])
print(my_list[::-1])
print(my_list[::-2])
