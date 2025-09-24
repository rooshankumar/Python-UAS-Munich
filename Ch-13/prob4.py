def divisible5(num):
    if num % 5 == 0:   # use num instead of n
        return True
    else:
        return False

a = [12, 43, 55, 66, 15, 10, 90]
f = list(filter(divisible5, a))
print(f)
