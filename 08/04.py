def german(a, b, c):
    res = (a + b) * c
    print(res)
    return res


...
a = 10
b = 5
c = 8
german(a, b, c)
...
d = 88
german(10, a, d)
...
result = german(99, 9, 2)
...
german(result, d, b)
...
