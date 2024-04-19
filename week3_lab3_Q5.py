student_name = []  # List to store student names
student_age = []   # List to store student ages

# Loop to ask for input 7 times
for i in range(0,7):
    name = input("Please provide your name: ") # Get name input from user
    age = input("Please provide your age:") # Get age input from user

    # Appending inouts to the empty lists
    student_name.append(name)
    student_age.append(age)

## For loop option to display student names and ages
for i in range(0,7):
    if student_age[i] == "20": # Check if age is "20"
        break  # Exit the loop if age is "20"
        print(student_name[i], student_age[i])  # Print name and age

# While loop option to display student names and ages
i = 0
while i < 7 and student_age[i] != "20":  # Check condition for age and loop limit
    print(student_name[i], student_age[i])  # Print name and age
    i += 1  # Increment loop counter