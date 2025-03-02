#Program to print only the added fraction of any two number {Input: 2.356, 3.5678 Output:0.9238}

num1=float(input("Enter the 1st number:"))
num2=float(input("Enter the 2nd number:"))
F1= num1 - int(num1)
F2= num2 - int(num2)
Add = F1+F2
print("The added fraction of two is:",Add)
