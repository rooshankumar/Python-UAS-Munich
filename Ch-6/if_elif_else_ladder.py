#If Elif else Ladder
a = int(input("Enter your age : "))

if( a > 18):
    print("You are an Adult.")
    print("Congrats ! ")

elif(a<0):
    print("You are a Dumb.\n Please write your correct age.")

elif(a==0):
    print("Opppps! Dumb is here.\n Please write your correct age.")

else: 
    print("You are a Teenager")


print("End of Program.")