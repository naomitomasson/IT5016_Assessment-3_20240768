# Define a function named rand
def rand():
    import random  # Import the random module to generate random numbers
    value = random.randint(0, 20)  # Generate a random integer between 0 and 20
    print(value)  # Print the generated random value
    return value  # Return the generated random value


# Call the rand function to generate and print a random value
rand()
