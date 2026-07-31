a = -1001
c = 10
result = None

# if a > 0 and c == 0:  # True and False = False   1 * 0 = 0
if a > 0 or c == 0:  # False or False = False   0 + 0 = 0
    result = a + 10
else:
    result = a + 20


print(result)
