my_string = """Цей текст є прикладом рядка, який містить кириличні символи.
Це новий рядок тексту, який також містить кириличні символи.
І ще один рядок тексту з кириличними символами.
Це останній рядок тексту, який містить кириличні символи.
"""


with open("output_3.txt", "w") as f:
    f.write(my_string)


with open("output_3.txt", "r") as f:
    data_1 = f.read(10)
    data_2 = f.read(5)
    data_3 = f.read(55)

print(data_1)
print(data_2)
print(data_3)

with open("output_3.txt", "rb") as f:
    data_1 = f.readline()
    data_2 = f.readline()
    data_3 = f.readline()

print(data_1.decode("Windows-1251"))
print(data_2.decode("Windows-1251"))
print(data_3.decode("Windows-1251"))


with open("output_3.txt") as f:
    data_all = f.readlines()

print(data_all)
print("----------")
for line in data_all:
    print(line.strip())
