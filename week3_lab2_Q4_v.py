
city=[]         #empty array
i = input("Please give me the names of 5 cities:")
city = i.split()  #spliting the string by spaces

city.pop(0)  #this takes "city" array and "pops" the first value (0) off of the list the input from user
             # becuse we are returned an array or list but there is not already one in the
             #code we cannot use "xyz.remove()" -this can only be used for arrays.
print (city)