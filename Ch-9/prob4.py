# Simple replacement program

# File paths
input_file = "Ch-9/file.txt"
output_file = "Ch-9/text.txt"

# Read the content
with open(input_file, "r") as f:
    content = f.read()

# Replace "donkey" with "#######"
content_new = content.replace("donkey", "#######")

# Write to a new file
with open(output_file, "w") as f:
    f.write(content_new)

print("Replacement done! Check 'text.txt'")
