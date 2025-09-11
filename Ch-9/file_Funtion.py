import os

file_path = "Ch-9/file.txt"

# Ensure the directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# ==============================
# 1. Write to a file (overwrite mode)
# ==============================
def write_file():
    content = """Hey you are doing a awesome job.
What is your name?
Where are you from?
How old are you?
Do you work or study?
"""
    with open(file_path, "w") as f:
        f.write(content)
    print("File written successfully!")

# ==============================
# 2. Append content to the file
# ==============================
def append_file():
    more_content = "\nThis line is appended to the file."
    with open(file_path, "a") as f:
        f.write(more_content)
    print("Content appended successfully!")

# ==============================
# 3. Read the whole file at once
# ==============================
def read_file():
    try:
        with open(file_path, "r") as f:
            content = f.read()
        print("Reading entire file:")
        print(content)
    except FileNotFoundError:
        print("File not found!")

# ==============================
# 4. Read the file line by line
# ==============================
def read_line_by_line():
    try:
        with open(file_path, "r") as f:
            print("Reading line by line:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("File not found!")

# ==============================
# 5. Read all lines into a list
# ==============================
def read_lines():
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        print("Reading all lines into a list:")
        print(lines)
    except FileNotFoundError:
        print("File not found!")

# ==============================
# 6. Check if the file exists
# ==============================
def check_file_exists():
    if os.path.exists(file_path):
        print("File exists!")
    else:
        print("File does not exist!")

# ==============================
# Main function to run all
# ==============================
def main():
    check_file_exists()
    write_file()
    append_file()
    read_file()
    read_line_by_line()
    read_lines()

if __name__ == "__main__":
    main()
