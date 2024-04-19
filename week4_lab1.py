# Prompt the user to input their first name, last name, and ID
name1= input("Please tell us your first name.")
name2= input("Please tell us your last name.")
id= input("Please tell us your id.")

# Prompt the user to input why they're here
intro= input("Please tell us why you're here.")

# Split the input intro into a list of words
reply= intro.split()

# Generate an ID by adding the first two characters of the input ID and the
# first three characters of the last name
idgenerator= id[:2] + " " + name2[:3]

# Create a counter variable
i = 0

# Iterate through each word in the reply list
for a in reply:
    # Check if the word is "Whitecliffe" and "College"
    if a == "Whitecliffe" and "College":
        # If both words are present, print the generated ID
        print (idgenerator)
        # Increment the counter
        i = i + 1