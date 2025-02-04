#write the program to check given no is divisible by 3 and 4 and print Good morning,only divisible by 3 and print Good afternoon, only divisible by 4 print Good evening else print Good night

num = int(input("Enter the number: "))
if(num%3==0 and num%4==0):
    print("Good Morning")
elif(num%3==0):
    print("Good Afternooon")
elif(num%4==0):
    print("Good Evening")
else:
    print("Good Night")
    

