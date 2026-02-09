import os

while True:
    filename = input("Enter the file name: ")

    if os.path.isfile(filename):
        print(f"The file '{filename}' exists.")
        break
    else:
        print(f"The file '{filename}' does not exist. Please try again.\n")
