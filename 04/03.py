number_1 = input("Введите первое число ")
number_2 = input("Ведите второе число ")
number_1 = int(number_1)
number_2 = int(number_2)
operator = ""
while operator not in ["+", "-", "*", "/"]:
    operator = input("Какую операцию вы хотите? ")
if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    if number_2 == 0:
        print("Деление на 0 запрещено ")
    else:
        print(number_1 / number_2)
else:
    print("Неверная операция ")


number = int(input("Введіть число: "))
print("Квадрат числа:", number ** 2)

# print("Середнє:", (number_1 + number_2 + number_3) / 3)
