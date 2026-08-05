import copy

s = 3
a = [3, 56, [3, 4, 5], "34"]
d = copy.deepcopy(a)
a[2].append(99)

a.append(0)
print(a)
print(d)
