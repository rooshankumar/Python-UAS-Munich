with open("Ch-9/this.txt") as f:
    content = f.read()

with open("Ch-9/that.txt","w") as f:
    f.write(content)