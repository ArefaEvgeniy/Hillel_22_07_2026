my_string = "Цей текст є прикладом рядка, який містить кириличні символи."

f = open("output.txt", "w", encoding="utf-8")
f.write(my_string)
f.close()

german = open("output.txt", encoding="utf-8")
data = german.read()
german.close()

print(data)
