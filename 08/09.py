def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
    print("-------------------")


func()
func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
func(7)
func(7, 8, f=145, a=45, u=88)
func(f=145, a=45, u=88)
