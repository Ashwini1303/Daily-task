'''An ATM contains Indian currency notes of 100 500 and 1000 To withdraw cash from this ATM,
the user has to enter the number of notes he/she wants of each currency, i.e., of 100
500 and 1000 Write a program to calculate the total amount withdrawn by the person
from the ATM in rupees'''

Currency_100 = int(input("Enter the no of currency in 100: "))
Currency_500 = int(input("Enter the no of currency in 500: "))
Currency_1000 = int(input("Enter the no of currency in 1000: "))
Withdraw_cash_amount = Currency_100 *100 +Currency_500 *500 +Currency_1000 *1000
print("The total amount withdraw from ATM:",Withdraw_cash_amount)

