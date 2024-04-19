class Demo:
    # Class variable to track count
    static_counter = 2

    def __init__ (self):
        # Increment the static_counter by 1
        Demo.static_counter += 1
        # Assign the value of the static counter to self.variable_counter
        self.variable_counter = Demo.static_counter

#Can do for i in range(any number) to get all the numbers sequentially from the start
# The class Demo = x
x = Demo()
# Print the values from the varable_counter
print(x.variable_counter)