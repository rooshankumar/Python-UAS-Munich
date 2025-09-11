# f = open("Ch-9/myfile.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this:
with open("Ch-9/myfile.txt") as f:
    print(f.read())

    # with this no need to write f.close()


