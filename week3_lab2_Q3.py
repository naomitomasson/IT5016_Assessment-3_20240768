# Defining lists of car names and colours
cars = ["audi", "merc", "porsche"]
colours = ["blue", "red", "pink", "black"]

# Nested loops to iterate through each combination of cars and colors
for b in cars: # Loop through each car in the 'cars' list
    for c in colours: # Nested loop to iterate through each color in the 'colours' list
        print(b,c) # Print the combination of the current car and color