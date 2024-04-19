class Arithmetic:
    def __init__(self,firstnumber, secondnumber):
        # Start with two values: first and second number
        self.firstnumber = firstnumber
        self.secondnumber = secondnumber

    def add(self):
        # Method to add the two numbers
        return(self.firstnumber + self.secondnumber)

    def subt(self):
        # Method to subtract the second number from the first
        return(self.firstnumber - self.secondnumber)

    def div(self):
        # Method to divide the fist number by the second number
        return(self.firstnumber/self.secondnumber)

# Calling the class with the chosen cariable of 60 being firstnumber and 35 being second number
ans = Arithmetic(60, 35)
# Call the add method and print the result
print(ans.add()) # Output: 95
# Call the div method and print the result
print(ans.div()) # Output: 1.7142857142857142
