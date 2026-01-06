import math

# Addition

a = int(input("Enter first number-"))
b = int(input("Enter second number-"))
print(f"Addition: {a + b}")

# Subtraction

a = int(input("\nEnter first number-"))
b = int(input("Enter second number-"))
print(f"Subtraction: {a - b}")

# Multiplication

a = int(input("\nEnter first number-"))
b = int(input("Enter second number-"))
print(f"Multiplication: {a * b}")

# Division

a = int(input("\nEnter numerator-"))
b = int(input("Enter denominator-"))
if b != 0:
    print(f"Division: {a / b}")
else:
    print("Division by zero is not allowed!")

# Area of Triangle

base = int(input("\nEnter base of triangle: "))
height = int(input("Enter height of triangle: "))
print(f"Area of Triangle: {0.5 * base * height}")

# Area of Circle

radius = int(input("\nEnter radius of circle: "))
print(f"Area of Circle: {math.pi * radius ** 2:.2f}")