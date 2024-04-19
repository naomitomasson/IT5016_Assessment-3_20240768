def identity():
    # Create empty dictionary
    ids ={}
    for i in range(3): # Loop 3 times (ask for 3 inputs

        # Retrive user input
        name = input("please enter your name:")
        regnum = input("please enter your reg number:")

        # Take empty dictionary and add values to keys form input
        ids[name] = regnum
    # Print dictionary
    print (ids)

# Call function
identity()