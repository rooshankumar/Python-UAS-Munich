def fahrenheit_to_celsius(f):
    c = (5/9) * (f - 32)
    return c

f = float(input("Enter the temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print(f"{f}°F is equal to {c:.2f}°C")
