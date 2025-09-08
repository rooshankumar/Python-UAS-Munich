marks = int(input("Enter your marks : "))

if marks >= 90 and marks <= 100:
    grade = 'A'
elif marks >= 80 and marks < 90:
    grade = 'B'
elif marks >= 70 and marks < 80:
    grade = 'C'
elif marks >= 60 and marks < 70:
    grade = 'D'
elif marks >= 50 and marks < 60:
    grade = 'E'
elif marks >= 0 and marks < 50:
    grade = 'Fail'
else:
    grade = 'Invalid marks'

print("Your grade is :", grade)
