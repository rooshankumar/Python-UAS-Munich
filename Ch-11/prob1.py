# Base class for 2D vector
class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector i={self.i}, j={self.j}")

# Derived class for 3D vector inheriting from TwoDvector
class ThreeDvector(TwoDvector):  # Inherit from TwoDvector
    def __init__(self, i, j, k):
        super().__init__(i, j)  # Call TwoDvector's constructor
        self.k = k              # Additional attribute for 3D vector

    def show(self):
        print(f"The vector i={self.i}, j={self.j}, k={self.k}")

# Create objects
a = TwoDvector(2, 3)
b = ThreeDvector(4, 5, 6)

# Display vectors
a.show()  # Output: The vector i=2, j=3
b.show()  # Output: The vector i=4, j=5, k=6
