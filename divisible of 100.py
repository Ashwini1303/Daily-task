'''You have a number in hand, and your challenge is to write a program that determines whether this number can be evenly divided by 100. Can you uncover if it‟s a 
multiple of 100 or not?
'''

num = int(input("Enter the number:"))
if(num %100==0):
    print(f"{num} is a multiple of 100")
else:
    print(f"{num} is not a multiple of 100")
