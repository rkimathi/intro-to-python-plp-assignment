# PLP Academy Python Week 1 Assignment

# Basic Calculator Program
# Basic Calculator Program for Integer Input

# Ask the user to input the first number (integer)
num1 = int(input("Enter the first integer: "))

# Ask the user to input the second number (integer)
num2 = int(input("Enter the second integer: "))

# Ask the user to input the operation they want to perform
operation = input("Enter the operation (+, -, *, /): ")

# Perform the corresponding mathematical operation based on user input
if operation == '+':
    result = num1 + num2  # Addition
    print(f"{num1} + {num2} = {result}")

elif operation == '-':
    result = num1 - num2  # Subtraction
    print(f"{num1} - {num2} = {result}")

elif operation == '*':
    result = num1 * num2  # Multiplication
    print(f"{num1} * {num2} = {result}")

elif operation == '/':
    if num2 != 0:  # Check to avoid division by zero error
        result = num1 // num2  # Integer Division
        print(f"{num1} / {num2} = {result} (Integer Division)")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Error: Invalid operation. Please enter +, -, *, or /.")
