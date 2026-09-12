def func(**kwargs):
    print("kwargs:", kwargs)
    print("-------------------")


a = 55
func(a=66, c=4, b=0)
func(a=66, c=4, b=0, r=99, p=a)
func(a=66)
func()
