# Read the old file
with open("Ch-9/old.txt", "r") as f:
    content = f.read()

# Write to a new file
with open("Ch-9/renamed_by_Python.txt", "w") as f:
    f.write(content)

print("File has been copied and renamed successfully!")
