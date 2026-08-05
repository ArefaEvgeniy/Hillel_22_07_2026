import copy


a = [3, 56, -7, "34"]
b = a.copy()
c = a[:]
d = copy.copy(a)

print(id(a))
print(id(b))

a.append(0)
print(a)
print(b)
print(c)
print(d)
