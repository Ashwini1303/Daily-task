'''
Write a program to implement calculator program with 5 basic arithmetic operations with input choice as a character (e.g. use 'a' for addition, 's' for subtraction, 'm' for 
multiplication, 'd' for division and 'u' for modulus operation, which gives the reminder of the division). 
For example, consider two number 20 and 15 and an input "a". "a" means addition, so, 20a15 = 20 + 15 = 35.
For example, consider two number 20 and 15 and an input "u". "u" means modulus, so, 20u15 = 20 mod 15 =5.
'''

def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (a for addition, s for subtraction, m for multiplication, d for division, u for modulus): ").lower()
  
    if operation == 'a':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == 's':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == 'm':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == 'd':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero")
    elif operation == 'u':
        if num2 != 0:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        else:
            print("Error: Modulus by zero")
    else:
        print("Invalid operation choice. Please enter a valid operation.")
        
calculator()
