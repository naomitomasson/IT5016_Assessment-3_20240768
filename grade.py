# Get input from the user for four grades and convert them to integers
m1 = int(input("enter m1"))
m2 = int(input("enter m2"))
m3 = int(input("enter m3"))
m4 = int(input("enter m4"))

# Calculate the average
final_grade = (m1 + m2 + m3 + m4)/4

# Check if the final grade is less than 50, if it is print "FAIL"
# else print "PASS
if (final_grade <50):
    print("FAIL")

else:
    print("PASS")