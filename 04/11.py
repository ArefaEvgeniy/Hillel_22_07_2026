number = int(input("Введите положительное число: "))
sum = 0

while number > 0:
    if number % 3 == 0:
        number -= 1
        continue
    sum += number ** 2
    if sum >= 1000:
        sum -= number ** 2
        break
    number -= 1
else:
    print("Цикл завершился без прерывания.")

print("Сумма квадратов чисел:", sum)
