# Define a function named calculation that calculates the percentage from the given marks
def calculation(m1, m2, m3, m4):
    # Calculate the total sum of the marks
    total = m1 + m2 + m3 + m4
    # Calculate the average by dividing the total sum by the number of marks (4)
    per = total / 4
    # Print the calculated percentage
    print("Your percentage is:", per)
    # Return the calculated percentage
    return per

# Define a function named fail_or_pass that determines if the percentage is below 50% (fail) or not (pass)
def fail_or_pass(per):
    # Check if the percentage is less than 50
    if per < 50:
        print("You failed :(")  # Print a failure message if the percentage is less than 50
    else:
        print("You passed! :)")  # Print a success message if the percentage is 50 or higher

# Prompt the user to input marks for four subjects
m1 = int(input("please type mark 1:"))  # Input mark 1
m2 = int(input("please type mark 2:"))  # Input mark 2
m3 = int(input("please type mark 3:"))  # Input mark 3
m4 = int(input("please type mark 4:"))  # Input mark 4

# Calculate the percentage from the input marks
percentage = calculation(m1, m2, m3, m4)
# Determine whether the user passed or failed based on the calculated percentage
fail_or_pass(percentage)