my_string_1 = "I'd  like          PYTHON i    likesi"

print(my_string_1.split())
print(my_string_1.split("i"))

new_list = my_string_1.split()
print(" ".join(new_list))
print("---".join(new_list))
print("".join(new_list))
