# Defining a function with any number of inputs
def percentage(*args):
    sum = 0
    for i in args:
        sum = sum + i # Iterating through the input values and adding each number each iteration

    avg = sum / len(args)     # Dividing the total sum by how many items were in the input
    print("average = ", avg)  # Printing the result
    return avg # Returning the result


# Defining a function to determine weather the average number means a pass or a fail
def pass_or_fail(per):

    for x in per: # Calculating if the total from the percentage function
                  # is higher or lower than 50 to determine the pass or fail result
        if x <50:
            # If higher than 50 print 'Pass'
            print("Pass")
        else:
            # If it is less than 50 print 'Fail'
            print("Fail")


# Calling the percentage function with the grades on 25, 35 and 65
per = percentage(25, 35, 65)
# Calling the pass or fail function
pass_or_fail # Output: average =  41.666666666666664