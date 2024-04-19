# Define a function that asks for inputs and performs calculations on them
    def calculation(x, y, z):
        # Create a list containing the three input numbers
        numbers = [(x), (y), (z)]  # turning the integers from input into an array
        # Calculate the sum of the three numbers
        total = x + y + z
        # Get the length of the numbers list (which is always 3)
        length = len(numbers)
        # Print the total of the numbers
        print("The total of your numbers is:", total)
        # Print the number of input numbers
        print("You input", length, "numbers.")

    # Prompt the user to input three numbers
    x = int(input("Can you give me 1 number?"))  # Input the first number
    y = int(input("Can you give me 1 number?"))  # Input the second number
    z = int(input("Can you give me 1 number?"))  # Input the third number

    # Call the calculation function with the provided input numbers
    calculation(x, y, z)