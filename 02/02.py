a = 7
print(id(a))
b = a
a = "Liberty"
print(id(a))
a = a + "RR"
print(id(a))
a = "STOP"
print(id(a))
c = 7
print(id(b))
print(id(c))

x = "Liberty"
print(id(a))
print(id(x))

y = 1004
print(id(y))
