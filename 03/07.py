age = input("What is your age: ")

if not age.isdigit() or int(age) <= 0:
    print("Please enter a valid non-negative integer for age.")
elif int(age) <= 10:
    print("Milk")
elif int(age) < 18:
    print("Juice")
elif int(age) < 100:
    print("Beer")
else:
    print("Water")


# if not age.isdigit() or int(age) <= 0:
#     print("Please enter a valid non-negative integer for age.")
# elif int(age) > 0 and int(age) < 10:
#     print("Milk")
# elif int(age) > 10 and int(age) < 18:
#     print("Juice")
# elif int(age) > 18 and int(age) < 100:
#     print("Beer")
# else:
#     print("Water")
