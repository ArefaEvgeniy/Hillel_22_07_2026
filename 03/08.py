a = 10
res = None

if a > 0:
    print("Positive")
    res = True
else:
    print("Non-positive")
    res = False
print(res)


print("Positive") if a > 0 else print("Non-positive")
res_2 = True if a > 0 else False
print(res_2)
