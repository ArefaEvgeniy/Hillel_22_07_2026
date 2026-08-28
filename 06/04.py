my_dict = {"YYY": 34, 56: 0, 99: "RRR", (1, 2, 3): ["Hello", "World"]}
my_list = [1, "hello", [3, 4, 5], 99]

my_dict.update({"name": "Bob", "age": 56})
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print("-" * 20)
for item in my_dict:
    print(my_dict[item])

print("-" * 20)
for item in my_dict.values():
    print(item)

print("-" * 20)
for key, value in my_dict.items():
    print(key, value)
