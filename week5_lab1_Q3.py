# Define a function named average that calulates the addition of all
# key word arguments and divides them by the length of **kwargs
def average(**kwargs):
    total = sum(kwargs.values()) #will select kwargs values only using .values and add them together
    avg = total / len(kwargs) #dividing the toal by the length of **kwargs
    return avg # Return the average
    print(avg) # Print the average

# Call the average function with the below key word arguments
k = average(IT5014=60, IT7809=80, IT6798=50, IT5048=70)
# Print the average
print(k)