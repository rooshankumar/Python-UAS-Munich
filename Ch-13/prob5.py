from functools import reduce

a = [12, 43, 55, 66, 15, 10,  5555, 90]

def greater(a, b):
    if a > b:
        return a
    else:
        return b   

print(reduce(greater, a))
