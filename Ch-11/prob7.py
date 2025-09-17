class Vector:
    def __init__(self, l):
        self.l = l  # Store the vector as a list

    def __len__(self):
        return len(self.l)  # Return the length of the vector

    def __str__(self):
        return f"{self.l}"  # String representation of the vector

# Create an instance of Vector
v1 = Vector([1, 2, 3, 4])

# Use the len() function on v1
print(len(v1))  # Output: 4

# Print the vector
print(v1)       # Output: [1, 2, 3, 4]
