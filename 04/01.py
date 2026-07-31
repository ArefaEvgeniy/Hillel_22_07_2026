my_list = [1, 2.23, [0, 99, "RRR"], 100, -44, "Hello", True]

print(my_list)
print(type(my_list))
print(len(my_list))

my_list.append("New Element")
print(my_list)
my_list.insert(2, "Inserted Element")
print(my_list)

print(my_list[3])
print(my_list[3][1])

my_list.pop()
print(my_list)

my_list.pop(0)
print(my_list)

my_list.remove(100)
print(my_list)
