new_age = 4445

print("Next year, you will be", new_age)
print()
print(45, 66, 7889, "#$$", sep="   ", end=" ")
print(new_age)
print("WWW", sep="!!!")

my_file = open("output.txt", "w")
print(45, 66, 7889, "#$$", sep="   ", file=my_file)
my_file.close()
