# Import the randint function to generate random integers
from random import randint

# Define the Train class
class Train:
    # Method to book a train ticket (using 'this' instead of 'self')
    def book(this, train_no, trainfrom, trainto):
        print(f"The ticket is booked from {trainfrom} to {trainto} in train number {train_no}")
    
    # Method to check the train's status (using 'this' instead of 'self')
    def status(this, train_no):
        print(f"The train number {train_no} is on time")

    # Method to calculate and display the fare from one station to another (using 'this' instead of 'self')
    def fare(this, train_no, trainfrom, trainto):
        print(f"The fare from {trainfrom} to {trainto} in train number {train_no} is {randint(222, 5000)}")

# Create an instance of Train named 't'
t = Train()

# Call the book method
t.book(12345, "Delhi", "Mumbai")
# Output: The ticket is booked from Delhi to Mumbai in train number 12345

# Call the status method
t.status(12345)
# Output: The train number 12345 is on time

# Call the fare method
t.fare(12345, "Delhi", "Mumbai")
# Output: The fare from Delhi to Mumbai in train number 12345 is <random_number_between_222_and_5000>
