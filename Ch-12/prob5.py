n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]
with open("Ch-12/tables.txt", "w") as file:
    for line in table:
        file.write(f"{line}\n")
print("Multiplication table written to Ch-12/tables.txt")