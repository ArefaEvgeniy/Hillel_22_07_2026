temp_1 = "My name is {}. I am {} years old. Name {} is the best name!"
temp_2 = "My name is {0}. I am {1} years old. Name {0} is the best name!"

name = "Nick"
age = 25

print(temp_1.format(name, age, name))
print(temp_1.format('Bob', 'Kate', age))
print(temp_2.format(name, age))
