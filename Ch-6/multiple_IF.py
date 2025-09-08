a = int(input("Enter your age : "))

# IF statement no. 1
if(a%2 == 0):
    print("a is even.")
#End of IF statement no. 1

# IF statement no. 2
if( a > 18):
    print("You are an Adult.")
    print("Congrats ! ")

elif(a<0):
    print("You are a Dumb.\n Please write your correct age.")

elif(a==0):
    print("Opppps! Dumb is here.\n Please write your correct age.")

else: 
    print("You are a Teenager")
#End of IF statement no. 2


print("End of Program.")