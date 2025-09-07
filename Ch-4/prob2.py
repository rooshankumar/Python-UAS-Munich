marks = []

m1 = int(input("Enter Marks : "))
marks.append(m1)

m2 = int(input("Enter Marks : "))
marks.append(m2)

m3 = int(input("Enter Marks : "))
marks.append(m3)

m4 = int(input("Enter Marks : "))
marks.append(m4)

m5 = int(input("Enter Marks : "))
marks.append(m5)

print("Before sorting:", marks)

marks.sort()  # Sorts the list in-place

print("After sorting:", marks)  # Print the sorted list
