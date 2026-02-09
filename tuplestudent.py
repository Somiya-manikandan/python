 
roll_numbers = (1, 2, 3)

student_names = ["lokesh", "somiya", "dhanush"]
students_dict = dict(zip(roll_numbers, student_names))
print("Initial data:")
print("Roll Numbers Tuple:", roll_numbers)
print("Student Names List:", student_names)
print("Students Dictionary:", students_dict)
new_roll = int(input("\nEnter a new roll number: "))
new_name = input("Enter the student name: ")

roll_numbers = roll_numbers + (new_roll,)
student_names.append(new_name)
students_dict[new_roll] = new_name
print("\nUpdated data:")
print("Roll Numbers Tuple:", roll_numbers)
print("Student Names List:", student_names)
print("Students Dictionary:", students_dict)
