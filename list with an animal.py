animals = ["dog", "cat", "elephant", "lion", "tiger"]
print("zero index position:", animals[0])
print(" first index position:", animals[1])
print("3rd position:", animals[3])
removed_element = animals.pop(3)
print("removed :", removed_element)
del animals[3]
animals.sort()
print("Sorted list with index positions:")
for index, value in enumerate(animals):
    print(index, value)
