import random
class Membership:
    id_number = 100 # Variable to keep track of membership numbers starting from 100

    def __init__(self):
        #All variable currently don't have a value assigned to them accept self.status
        self.student_id = None
        self.lastname = None
        self.program = None
        self.new_id = None
        self.status = 'Active' # Default status is set to 'Active'

    def data(self):
        # Gather details from student
        self.student_id = input("Please enter your Whitecliffe ID:")
        self.lastname = input("Please enter your last name:")
        self.program = input("Please enter your study program name:")
        # generating a new ID number by calling the below function
        self.new_id = self.generate_membership()

    def generate_membership(self):
        # List of registered students
        registered_student = ['S1','S2','S3','S4','S5']
        #Check if student ID entered into self.student ID above matches one in the list
        if self.student_id in registered_student:
            #If yes then do the following
            # The class variable at the top has incremented by 1 and this is the new assigned ID
            Membership.id_number += 1
            self.variable_counter = Membership.id_number
            return self.variable_counter

        #else print declined entry as user is not a registered sudent
        else:
            print("Declined entry")
            return None


    def display(self):
        # Printing a display of all the student details
        if self.student_id:
            print(self.student_id)
            print(self.lastname)
            print(self.program)
            print(self.new_id)
            print(self.status)


    def withdrawal(self,ln):
        #Withdraw the student if the last name provided matches
        if self.lastname == ln:
            self.status ='Withdrawn'
            return self.status


registration = []
num = int(input("How many students are enrolling today?"))
# For the amount in num execute the following
for i in range(num):
    k = Membership()
    k.data()
    registration.append(k)


name = (input("Who is the student withdrawing today?"))
# For the amount in name update the following
for i in range(num):
    registration[i].withdrawal(name)
    registration[i].display()


# Counter statistics
active=0
withdrawn=0
diploma=0
bachelor=0
# Iterate through each registered student
for i in range(num):
    # Check the status of each student and increment the respective counter
    if registration[i].status=="Active":
        active+=1
    if registration[i].status=="Withdrawn":
        withdrawn += 1
    if registration[i].status=="Diploma":
        diploma += 1
    if registration[i].status=="Bachelor":
        bachelor += 1


# Display statistics
print('......Statistics......')
print('The number of active numbers is: ', active)
print('The number of withdrawn students is: ', withdrawn)
print('The number of members in the Diploma is: ', diploma)
print('The number of members in the Bachelor programme is: ', bachelor)


# Creating a new membership and displaying its details (calling the class)
x = Membership()
print(x.display)

