# Define a function named calculator that takes two numbers as input and performs addition and subtraction
def calculator(x, y):
    # Calculate the sum of the two numbers
    add = x + y
    # Calculate the subtraction of y from x
    sub = x - y
    # Print the result for addition
    print("Your numbers added together are:", add)
    # Print the result for subtraction
    print("Your numbers subtracted are:", sub)

# Prompt the user to input the first number
x = int(input("please provide your first number:"))
# Prompt the user to input the second number
y = int(input("please provide your second number:"))

# Call the calculator function with the provided input numbers
calculator(x, y)