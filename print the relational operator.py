'''
You have two secret numbers, and you need to figure out how they relate to each other using a set of special tools. Your challenge is to write a program that uses these tools—>, 
>=, <, <=, ==, and !=—to uncover all the secrets about how these numbers compare. How will you use each tool to solve the puzzle?
'''

a = int(input("Enter first secret number: "))
b = int(input("Enter second secret number: "))

print(f"{a} < {b} is {a < b}")
print(f"{a} <= {b} is {a <= b}")
print(f"{a} > {b} is {a > b}")
print(f"{a} >= {b} is {a >= b}")
print(f"{a} == {b} is {a == b}")
print(f"{a} != {b} is {a != b}")

