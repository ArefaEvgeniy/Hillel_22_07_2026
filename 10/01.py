def decorator(func):
    def wrapper():
        print("1111111111111111")
        func()
        print("22222222222222")
    return wrapper


def decorator_2(func):
    def wrapper():
        print("AAAAAAAAAAAA")
        func()
        print("BBBBBBBBBB")
    return wrapper


@decorator  # func = decorator(func)
def func():
    print("Hello, World!")


@decorator_2
@decorator
def func_2():
    print("This is another function.")


@decorator
def func_3():
    print("This is yet another function.")


func()
print("--------------------------------")
func_2()
print("--------------------------------")
func_3()
