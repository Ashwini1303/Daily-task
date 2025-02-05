'''
Simple interest is a quick method of calculating the interest charge on a loan. Simple interest is determined by multiplying the daily interest rate by the principal by
the number of days that elapse between payments. 

Simple interest formula is given by:  Simple Interest = (P x T x R)/100 
Example 1:
Input :  P = 10000
         R = 5
         T = 5
Output : 2500
'''

P = int(input("Enter the principal amount (P): "))  
R = int(input("Enter the rate of interest (R): "))  
T = int(input("Enter the time period (T) in years: ")) 
simple_interest = (P * T * R) // 100

print(f"The simple interest is: {simple_interest}")
