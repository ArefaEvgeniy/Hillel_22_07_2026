number = int(input("Введите положительное число: "))
sum = 0

while number > 0:
    sum += number ** 2
    # sum = sum + number ** 2
    number -= 1
    # number = number - 1

print("Сумма квадратов чисел:", sum)
