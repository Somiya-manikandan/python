filename = "output_loop.txt"
with open(filename, "w") as file:
    for i in range(5):
        line = input(f"Enter statement {i+1}: ")
        file.write(line + "\n")
print("\nFile contents:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
