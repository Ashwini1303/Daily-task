'''
Imagine you have two secret letters, „A‟ and „B‟. Your task is to write a program that uses different comparison tools to uncover how these letters relate to each other. Can you 
figure out which one is greater or less than the other? Use your program to solve this letter comparison mystery!
'''

letter1 = input("Enter the first secret letter: ")
letter2 = input("Enter the second secret letter: ")

print(f"{letter1} < {letter2} is {letter1 < letter2}")
print(f"{letter1} <= {letter2} is {letter1 <= letter2}")
print(f"{letter1} > {letter2} is {letter1 > letter2}")
print(f"{letter1} >= {letter2} is {letter1 >= letter2}")
print(f"{letter1} == {letter2} is {letter1 == letter2}")
print(f"{letter1} != {letter2} is {letter1 != letter2}")
