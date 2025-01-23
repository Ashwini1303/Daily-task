num1 = int(input("Enter the First number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the Third number: "))
if(num1>num2):
    if(num1>num3):
        print(f"The greater number is: {num1}")
    else:
        print(f"The greater number is: {num3}")
else:
    print(f"The greater number is: {num2}")
