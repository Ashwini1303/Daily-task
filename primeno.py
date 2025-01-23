num = int(input("Enter the number:"))
print(f"Not a Prime number : {num}" if((num%2==0 or num%3==0) or (num%2==0 and num%3==0)) else f"Prime number:{num}")
