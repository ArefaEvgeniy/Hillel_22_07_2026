my_list = [1, 2, 3, 4, 5, "45", "Hello", -100, 0, 8]

index = 0
sum = 0
while index < len(my_list):
    if isinstance(my_list[index], (int, float)) and my_list[index] % 2 == 0:
        sum += my_list[index]
    index += 1

print("Сумма четных чисел в списке:", sum)


sum = 0
for item in my_list:
    if isinstance(item, (int, float)) and item % 2 == 0:
        sum += item

print("Сумма четных чисел в списке:", sum)
