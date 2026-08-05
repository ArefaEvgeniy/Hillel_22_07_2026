number = int(input("Введите положительное число: "))
sum = 0

while number > 0:
    sum += number ** 2
    if sum >= 1000:
        sum -= number ** 2
        break
    number -= 1

print("Сумма квадратов чисел:", sum)
