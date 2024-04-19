
# A function named age18 that checks if the provided age is 18 or above
def age18 (age):
    try:
        # Loop through each element in the input age
    for i in age:
        # Check if the given age is less than 18
        if i <18:
            print("Must be 18") # Print a message indicating the age must be 18 or older
        else:
            print("Age approved")# Number provided is above 18

# Prompt the user to enter their age
age = input("Enter your age: ")
# Call the age18 function with the provided age input
age18()