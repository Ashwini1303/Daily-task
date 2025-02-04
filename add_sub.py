'''You have two numbers, and your challenge is to write a program that performs both addition and subtraction with them. However, if any subtraction results in a negative 
number, display it as a positive value. How will you tackle this and show the final results?
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
subtraction = abs(num1 - num2)

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
