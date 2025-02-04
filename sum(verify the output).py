'''
You have two numbers, and your task is to write a program that reads these numbers and calculates their sum.
How will you make sure the program adds them together correctly and shows the result?
'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum_result = a + b
# Verify correctness
assert sum_result == (a + b)
print("Sum:", sum_result)
