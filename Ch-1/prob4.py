import os

# specify the directory ('.' means current directory)
directory = "/workspaces/Python-UAS-Munich/Ch-1"

# get list of files and folders
contents = os.listdir(directory)

print("Contents of directory:", directory)
for item in contents:
    print(item)
