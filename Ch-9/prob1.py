f = open("Ch-9/poem.txt")
c = f.read()
if ("elephant" in c):
    print("Yes, the word 'Elephant' is in the file.")
else:
    print("No, the word 'Elephant' is not in the file.")


f.close()