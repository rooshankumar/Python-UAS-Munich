a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))
d = int(input("Enter 4th no. : "))

if(a>b and a>c and a>d):
    print("The greatest no. is : ",a)

elif(b>a and b>c and b>d):
    print("The greatest no. is : ",b)

elif(c>a and c>b and c>d):
    print("The greatest no. is : ",c)

elif(d>a and d>b and d>c):
    print("The greatest no. is : ",d)

print("End of Program.")