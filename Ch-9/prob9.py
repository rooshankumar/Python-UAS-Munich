with open("Ch-9/this.txt", "r") as f:
    content = f.read()

with open("Ch-9/that.txt", "r") as f:
    content2 = f.read()

if content == content2:
    print("Files are identical")
else:
    print("Files are different")