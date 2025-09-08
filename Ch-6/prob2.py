n1 = int(input("Enter first subject marks : "))
n2 = int(input("Enter second subject marks : "))
n3 = int(input("Enter third subject marks : "))

# Check for total percentage
total_percentage = ((n1 + n2 + n3) / 300) * 100

# Conditions: total percentage >= 40 and all subjects >= 33
if total_percentage >= 40 and n1 >= 33 and n2 >= 33 and n3 >= 33:
    print("You Passed the Examination, Congrats!!")
else:
    print("Better luck next time.")
