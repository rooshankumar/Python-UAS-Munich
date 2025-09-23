#using Walrus operator
if(n:= len([1,2,3,4,5])) > 3:
    print(f"List is too long with {n} elements, expected <= 3")