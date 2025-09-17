# Define a class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the '+' operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Method to display the point
    def display(self):
        print(f"Point({self.x}, {self.y})")

# Create two Point objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Add the two points using overloaded '+'
p3 = p1 + p2

# Display the result
p3.display()  # Output: Point(6, 8)
