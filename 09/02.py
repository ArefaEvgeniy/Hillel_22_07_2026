def apply_operation(operation, data):
    print(operation(data))


def square(x):
    return x ** 2


def double(x):
    return x * 2


number = 67

apply_operation(square, number)
apply_operation(double, number)
