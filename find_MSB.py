#Program to print the MSB digit of given number {Input :1567, Output: 1}

number = int(input("Enter a number: "))
number = abs(number)
while number >= 10:
    number //= 10  

print("The most significant digit (MSB) is:", number)
