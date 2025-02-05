'''
Write a Python program to implement a calculator that performs five basic operations: addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and modulus (`%`).
The program should take two numerical inputs and an operation symbol from the user, and perform the corresponding calculation using a functional approach
(e.g., dictionary mapping or lambda functions) instead of `if-else` or `switch-case`.
'''

def calculator(a, b, op):
    operations = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else "Error: Division by zero",
        '%': a % b if b != 0 else "Error: Modulus by zero"
    }
    return operations.get(op, "Invalid Operation")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /, %): ")

print("Result:", calculator(a, b, op))
