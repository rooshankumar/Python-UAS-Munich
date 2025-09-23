
try:
    with open("Ch-12/1.txt", "r") as file:
     print(file.read())
except Exception as e:
    print(f"Error: {e}")

try:
    with open("Ch-12/2.txt", "r") as file:
     print(file.read())
except Exception as e:
    print(f"Error: {e}")

try:
    with open("Ch-12/3.txt", "r") as file:
     print(file.read())
except Exception as e:
    print(f"Error: {e}")

print("File operations completed.")
