
#You have a number to examine, and your mission is to write a program that checks whether this number can be divided evenly by 27. Can you find out if it‟s a multiple of 27?


num = int(input("Enter a number: "))
print(f"{num} is a multiple of 27" if num % 27 == 0 else f"{num} is not a multiple of 27")
