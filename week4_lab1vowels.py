# Counting the number of vowels in a string

# Define the list of vowels
vowels = ["a","e","i","o","u"]

# Prompt the user to create a message
message = input("Please write your message.")

# Create a counter
i = 0

# Iterate through each character in the input message
for l in message:
    # Check if the current character is a vowel
    if l in vowels:
        # If the current character is a vowel, increment the counter
        i = i + 1

# Print the number of vowels found in the input message
print("the number of vowels is:", i)





