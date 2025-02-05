'''
You have a number (n), and your challenge is to write a program that prints out a sequence starting from 1 and going up to (n). How will you design your program to 
generate and display this sequence of numbers?
'''

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i, end=" ")
