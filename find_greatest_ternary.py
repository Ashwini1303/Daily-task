'''
You have three hidden numbers, and your mission is to find out which one is the greatest. Write a program that can reveal the highest of these three numbers.
Perform the above operation using ternary operator.
'''

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

print(f"{num1} is greater" if (num1 > num2 and num1 > num3) else (f"{num2} is greater" if num2 > num3 else f"{num3} is greater"))




