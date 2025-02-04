'''
Imagine you have two mysterious numbers. Your task is to write a program that reveals which one of them is the bigger one. How will you solve this puzzle?
'''

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
if a > b:
    print(f"{a} is bigger.")
elif b > a:
    print(f"{b} is bigger.")
else:
    print("Both numbers are equal.")
