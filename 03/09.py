a = 0

if a > 0:
    print("Positive")
elif a == 0:
    print("Zero")
else:
    print("Negative")


print("Positive") if a > 0 else (print("Zero") if a == 0 else print("Negative"))
