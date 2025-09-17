# Define a class to represent complex numbers
class Complex:
    def __init__(self, r, i):
        self.r = r  # Real part
        self.i = i  # Imaginary part

    # Overload the '+' operator
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    # Overload the '*' operator
    def __mul__(self, c2):
        # (a+bi) * (c+di) = (ac - bd) + (ad + bc)i
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    # Overload the 'str' method to print the complex number nicely
    def __str__(self):
        return f"{self.r} + {self.i}i"

# Create two complex numbers
c1 = Complex(1, 2)  # 1 + 2i
c2 = Complex(3, 4)  # 3 + 4i

# Add the two complex numbers
print(c1 + c2)  # Output: 4 + 6i
# Multiply the two complex numbers
print(c1 * c2)  # Output: -5 + 10i