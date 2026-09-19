# def func(a, b, c="0"):
def func(a: int, b: int, c: str = "0") -> bool:
    """
    This function takes two integers a and b, adds them together,
    multiplies the result by 2, and checks if the string representation
    of that result is equal to the string c.
    """
    res = (a + b) * 2
    return c == str(res)


print(func(2, 3, "10"))
print(func(2, 3, "yryfhfg"))
print(func.__doc__)
