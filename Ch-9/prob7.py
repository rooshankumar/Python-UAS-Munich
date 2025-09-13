with open("Ch-9/log.txt") as f:
    c = f.readlines()  # read all lines

line_num = 1
found = False

for line in c:
    if "Python" in line:
        print("Yes, 'Python' is present.", line_num)
        found = True
    line_num += 1

if not found:
    print("No, 'Python' is not present.")
