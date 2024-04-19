# Get input from the user for the total score and convert it to an integer
score = int(input("Please enter the total score:"))

# Check if the score is within the valid range of 0 to 100
if (score >= 0) and (score <= 100):
    # Check different grade conditions based on the score

    # If the score is 80 or higher, print "A"
    if score >= 80:
        print("A")

    # If the score is between 60 and 79, print "B"
    elif score >= 60:
        print("B")

    # If the score is between 50 and 59, print "C"
    elif score >= 50:
        print("C")

    # If the score is below 50, print "FAIL"
    else:
        print("FAIL")

# If the score is less than 0 or greater than 100), print "OUT OF RANGE"
else:
    print("OUT OF RANGE")
