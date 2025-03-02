#Write a program to read a four digit number through the keyboard and calculate the sum of its digits

num = int(input("Enter a four-digit number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10   

print("The sum of the digits is:", sum)


    
