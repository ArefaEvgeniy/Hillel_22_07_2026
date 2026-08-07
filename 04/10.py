number = int(input("Введите положительное число: "))
sum = 0

while number > 0:
    sum += number ** 2
    if sum >= 1000:
        sum -= number ** 2
        break
    number -= 1

print("Сумма квадратов чисел:", sum)

#
# 135 = 0:02:15
#
# 1 мин = 60 сек
# 1 час = 3600 сек
#
# //
# %

# time = int(input("Введите время в секундах: "))
#
# hours = time // 3600
# time = time % 3600
# minutes = time // 60
# seconds = time % 60
# print("Часов:", hours, "Минут:", minutes, "Секунд:", seconds)
