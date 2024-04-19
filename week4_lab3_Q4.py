# Define a function named calculation that calculates the percentage from the given numbers
def calculation(numbers):
    # Split the input numbers string into a list of integers
    arr = [int(x) for x in numbers.split()] # Convert each element to an integer after splitting the string
    # Calculate the sum of the numbers
    add = sum(arr)
    # Calculate the average by dividing the sum by the number of elements in the list
    per = add / len(arr)
    print("Your percentage is:", per) # Print the calculated percentage
    return per # Return the calculated percentage

# Define a function named fail_or_pass that determines if the percentage is below 50% (fail) or not (pass)
def fail_or_pass(per):
    # Check if the percentage is less than 50
    if per < 50:
        print("You failed :(")  # Print a failure message if the percentage is less than 50
    else:
        print("You passed! :)")  # Print a success message if the percentage is 50 or higher

# Prompt the user to input marks
numbers = input("Please type marks:")
# Calculate the percentage from the input marks
percentage = calculation(numbers)
# Determine whether the user passed or failed based on the calculated percentage
fail_or_pass(percentage)