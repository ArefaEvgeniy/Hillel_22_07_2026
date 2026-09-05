a = [2, "44", 3.14, True, None]
b = (2, "44", 3.14, True, None)
c = {2, "44", 3.14, 0, "TTT", True, None}
d = {1: 2, 6: "44", 3.14: {2, 3, 55}, "P": 0, (5, 43): "TTT"}

print(c)
print(d[3.14])
print(d["P"])
