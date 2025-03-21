# Simple Calculator
num1 = float(input("Enter the first number: "))  
num2 = float(input("Enter the second number: "))  
operation = input("Enter the operation (+, -, *, /): ")  # This should appear after entering two numbers

if operation == '+':
    print("Result:", num1 + num2)
elif operation == '-':
    print("Result:", num1 - num2)
elif operation == '*':
    print("Result:", num1 * num2)
elif operation == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")

