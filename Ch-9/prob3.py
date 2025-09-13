def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{i} x {n} = {i*n}\n"
    with open(f"Ch-9/table-of-{n}.txt", "w") as f:
        f.write(table)

for i in range(2,20):
    generateTable(i)