a = 90
def fun():
    global a
    a = 20
    print(a)

print(a)
fun()