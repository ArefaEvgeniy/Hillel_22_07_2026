import copy


a = [3, 66, 0, ["rr", "TT"]]
b = copy.deepcopy(a)

print(b[3].append(1))

print(b)
print(a)
