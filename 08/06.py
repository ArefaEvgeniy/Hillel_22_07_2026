def func(*args):
    print("args:", args)
    res = 1
    for item in args:
        res *= item
    print("result:", res)
    print("----------")
    return res


func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
func(7)
func()
func(7, 8)
func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
