a = input("Enter your name : ")
b = input("Enter Today's Date :")

c = ''' Dear <|a|> \n
You are Selected \n
<|b|> '''

# Replace placeholders with actual values
letter = c.replace("<|a|>", a).replace("<|b|>", b)

# Print final letter
print("\n--- Final Letter ---")
print(letter)