filename = "output_no_loop.txt"
line1 = input("Enter statement 1: ")
line2 = input("Enter statement 2: ")
line3 = input("Enter statement 3: ")
line4 = input("Enter statement 4: ")
line5 = input("Enter statement 5: ")
with open(filename, "w") as file:
    file.write(line1 + "\n")
    file.write(line2 + "\n")
    file.write(line3 + "\n")
    file.write(line4 + "\n")
    file.write(line5 + "\n")
print("\nFile contents:")
with open(filename, "r") as file:
    print(file.read())
