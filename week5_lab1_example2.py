
#task/teacher example
def fruit_price(**kwargs):      # Using *kwargs means you can gather any amount of variables.
    sum = 0
    # Itterating through the dictionary and taking out the values
    # only and adding the current selected value to the previous total.
    for i  in kwargs.values():  # .values selects only the values in the dictionary not the keys
        sum = sum + i # The chosen value and adding it to the sum of previous
    return sum # Return result


# Calling the function with these keys and values
k = fruit_price(mango=10,Apple=5,Orange=15)
print(k) # Printing function fruit_price that was assigned to k

