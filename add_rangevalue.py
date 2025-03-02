#Program to calculate the sum from ‘M number to ‘N number.{Input M= 5 N= 10 ,Output =45}

M= int(input())
N= int(input())
Sum = 0
for i in range(M,N+1):
    Sum+=i
print(Sum)
