def decorator(func):
    def wrapper(*args, **kwargs):  # args=(5,), kwargs={'y': 7}
        print("1111111111111111")
        res = func(*args, **kwargs)  # func_3(5, y=7)
        print("22222222222222")
        return res
    return wrapper


@decorator
def func():
    print("Hello, World!")


@decorator
def summa(a, d):
    print(a + d)


@decorator
def func_3(a, y):
    return a + y


func()
print("--------------------------------")
summa(1, 2)
print("--------------------------------")
print(func_3(5, y=7))
