import copy


a = [3, 66, 0]

b = a.copy()
c = a[:]
d = copy.copy(a)

d.pop()
b.append("Hello")
c[0] = 99

print(a)
print(b)
print(c)
print(d)
