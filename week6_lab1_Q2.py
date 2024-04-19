class Cars:
    def __init__ (self, name, speed, mileage):
        #initialising the object with name, speed, and mileage attributes
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def nametag(self):
        # Method to print the name of the car
        print("Car name is: " + self.name)

    def milxten(self):
        # Method to calculate and return the mileage multiplied by 10
        return (self.mileage * 10)



# Running the class with the attributes: name:'audi', colour: 'red' and mileage: 10400
ten = Cars("audi", "red", 10400)
# Call the nametag method and print the name of the car
ten.nametag()# Output: Car name is: audi
# Call the milxten method to print the result
print(ten.milxten())# Output: 104000


