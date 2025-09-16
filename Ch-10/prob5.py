# Import the randint function to generate random integers
from random import randint

# Define the Train class
class Train:
    # Method to book a train ticket
    def book(self, train_no, trainfrom, trainto):
        print(f"The ticket is booked from {trainfrom} to {trainto} in train number {train_no}")
    
    # Method to check the train's status
    def status(self, train_no):
        print(f"The train number {train_no} is on time")

    # Method to calculate and display the fare from one station to another
    def fare(self, train_no, trainfrom, trainto):
        print(f"The fare from {trainfrom} to {trainto} in train number {train_no} is {randint(222, 5000)}")

# Create an instance of the Train class
t = Train()

# Book a ticket on train number 12345 from Delhi to Mumbai
t.book(12345, "Delhi", "Mumbai")
# Output: The ticket is booked from Delhi to Mumbai in train number 12345

# Check the status of train number 12345
t.status(12345)
# Output: The train number 12345 is on time

# Calculate and display the fare for the journey from Delhi to Mumbai on train number 12345
t.fare(12345, "Delhi", "Mumbai")
# Output: The fare from Delhi to Mumbai in train number 12345 is <random_number_between_222_and_5000>
