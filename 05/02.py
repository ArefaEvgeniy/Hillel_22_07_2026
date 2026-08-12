my_string_1 = "I'd like Python"
my_string_2 = 'I like "Python"'
my_string_3_1 = "I'd like "
my_string_3_2 = '"Python"'
my_string_3 = my_string_3_1 + my_string_3_2
my_string_4 = '''I'd like "Python"'''
my_string_5 = "I'd like \"Python\""
my_string_6 = "This is a multi-line string.\nIt can\tspan multiple lines."
my_string_7 = "This is a multi-line string.\\nIt can\\tspan multiple lines."
my_string_8 = r"This is a multi-line string.\nIt can\tspan multiple lines."
my_string_9 = """This is a multi-line string.
It can span multiple lines.
    It can also include indentation."""

print(my_string_1)
print(my_string_2)
print(my_string_3)
print(my_string_4)
print(my_string_5)
print(my_string_6)
print(my_string_7)
print(my_string_8)
print(my_string_9)

print("Go" * 10)
print(10 * "Go")

print(len(my_string_9))
print(len("I'd like \"Python\""))
print(len("I'd like Python"))
print("I'd like Python"[4:8])
print("I'd like Python"[7:3:-1])
