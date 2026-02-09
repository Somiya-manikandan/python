text = input("Enter a string: ")

space_count = 0

for ch in text:
    if ch == " ":
        space_count += 1

print("Number of spaces counted:", space_count)
