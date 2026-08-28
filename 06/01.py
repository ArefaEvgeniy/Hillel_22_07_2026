text = "Hello, world"
text_2 = "Привіт, світ"

print(type(text))
print(text.encode())
print(type(text.encode()))

new_text = text_2.encode("Windows-1251")
print(new_text)
print(text_2.encode("utf-8"))
print(type(new_text))

print(new_text.decode("Windows-1251"))
