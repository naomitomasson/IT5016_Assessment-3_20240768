# Defining a function with key word arguments
def fruit_price(**kwargs):

    for i, x in kwargs.items(): # Iterating through both keys and values in kwargs
                                # specifying i as keys and x as values by seperating with comma
        print(i)                #printing only i which has been assigned too keys


# Calling function with the below key word arguments
fruit_price(Mango=10,apple=5,Orange=15)
