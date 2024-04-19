#pseudocode: get input of items purchased at a supermarket and their values into a dictionary.
#use the values function to retrieve only the prices but ONLY from keys that begin with a vowel
#and add them together
#-5% off of that total
from typing import Any


def itemandcost():
    dictionary = {} # Create an empty dictionary
    for i in range(4): # Loop 4 times to get input for 4 items
        item = input("Please type an item from your cart:") # Get item name from the user
        price = int(input("Please tell us the price of that item:")) # Get item price from the user
        dictionary[item] = price # Add the item and its price to the dictionary
    print(dictionary)  # Print the dictionary (optional)
    return dictionary  # Return the dictionary containing items and prices

def add(dictionary):
    numbers = dictionary.values()  # Access the values of the input dictionary
    total = sum(numbers)  # Calculate the sum of all values in the dictionary
    return total  # Return the calculated total

def per(dictionary):
    vowels = 'AaEeIiOoUu' # Define a string containing vowels
    vowels_values = [] # Make an empty list to store prices of items whose keys start with a vowel
    for key in dictionary: # Iterate through keys in the dictionary
        if key[0] in vowels:  # Check if the first letter of the key is a vowel
            vowels_values.append(dictionary[key]) # If so, append its value to vowels_values list

    # Calculate the discount
    percentage = sum(vowels_values) * 20 / 100 # Calculate 5% of the total prices of items whose keys start with a vowel
    new_price = vowels_values - percentage # Calculate the new total price after applying the discount

    print ("The new price of these items is:" , new_price) # Print the new total price
    return new_price  # Return the new total price



# Call itemandcost() function to get the dictionary of items and prices
items_dict = itemandcost()
# Call add() function with the dictionary returned by itemandcost() to calculate the total cost
total_cost = add(items_dict)

print("The total cost of the items is:", total_cost)  # Print the total cost

# Call per() function with the dictionary returned by itemandcost() to calculate the discounted price
per(items_dict)
