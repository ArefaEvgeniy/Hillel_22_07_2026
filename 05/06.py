temp_1 = "My name is %s. I am %s years old. Name %s is the best name!"

name = "Nick"
age = 25

print(temp_1 % (name, age, name))
print(temp_1 % ('Bob', age, 'Kate'))
