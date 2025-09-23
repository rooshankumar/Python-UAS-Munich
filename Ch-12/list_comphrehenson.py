myList = [1,23,42,345,2345]

# squaredList = []
# for item in myList:
#     squaredList.append(item**2)

squaredList = [item**2 for item in myList]

print(squaredList)