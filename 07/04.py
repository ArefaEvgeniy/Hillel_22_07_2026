a = {1, 2, 3, 4, 5}
b = frozenset(a)

print(a)

a.pop()
print(a)

a.update([6, 7, 8])
print(a)
print(b)
