# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 10! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 1200
# print(factorial(n))

result = 1
while n > 1:
    result *= n
    n -= 1

print(result)
