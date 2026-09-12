def func_1():
    print("Hello, " + name + "!")


def func_2():
    def func_3():
        global name
        name = "Mike"
        print("Hello, " + name + ".")

    name = "John"
    print("Hello, " + name)
    func_3()


name = "David"
func_1()
func_2()
print("Bye, " + name)
