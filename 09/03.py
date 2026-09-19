# def func(a, b, c):
def func(a: int, b: int, c: str) -> bool:
# def func(a: int, b: str, c: float) -> None:
    res = (a + b) * 2
    return c == str(res)


print(func(2, 3, "10"))
print(func(2, 3, "yryfhfg"))
print(func.__annotations__)
