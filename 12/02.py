my_string = "Цей текст є прикладом рядка, який містить кириличні символи."


my_byte = my_string.encode("utf-8")
print(my_byte)
try:
    f = open("output_2.txt", "wb")
    f.write(my_byte)
finally:
    f.close()


with open("output_2.txt", "rt", encoding="Windows-1251") as german:
    data = german.read()

print(data)
