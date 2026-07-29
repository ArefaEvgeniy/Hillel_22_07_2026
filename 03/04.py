a = 1001
c = None
result = None

if a == 0:
    result = a + 10
    c = False
    if a > 1000:
        result = a
        c = 10
elif a > 100:
    result = a + 20
    c = 1
elif a > 0:
    result = a + 30
    c = 2
elif a < -100:
    result = a + 40
    c = 3
else:
    result = 0
    c = True
print(result)
print(c)
