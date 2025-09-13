# Simple replacement program
words = ["donkey", "table"]  # list of words to replace

# Read the content
with open("Ch-9/file.txt", "r") as f:
    content = f.read()

# Replace each word with '#' repeated for word length
for word in words:
    content = content.replace(word, "#" * len(word))

# Write to a new file
with open("Ch-9/file.txt", "w") as f:
    f.write(content)

print("Replacement done! Check 'file.txt'")
