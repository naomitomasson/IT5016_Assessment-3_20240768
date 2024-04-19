
#testing task code
# Define a class named Fruit
class Fruit:
    # Method to initialize with name and colour attributes
    def __init__(self, name, colour):
        self.name = name    # Assign the name of the fruit
        self.colour = colour    # Assign the colour of the fruit

    # Method to print the name of the fruit
    def func(self):
        print("Fruit is " + self.name)

# Calling the Fruit class with name "apple" and colour "red"
f1 = Fruit("apple", "red")
# Call the func method to print the name of the fruit
f1.func()# Output: Fruit is apple