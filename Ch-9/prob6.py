with open("Ch-9/log.txt") as f:
    c = f.read()

if "Python" in c:
    print("Yes, 'Python' is present.")
else:
    print("No, 'Python' is not present.")
