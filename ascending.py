
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

for num in range(n1, n2 + 1):
    if num % 2 == 0:
        print(num, end=" ")
