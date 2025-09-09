n = int(input("Enter number :  "))  # size of the square (3x3)

for i in range(1, n+1):
    for j in range(1, n+1):
        # print stars on the border
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # move to next line
