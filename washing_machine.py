'''
A washing machine works on the principle of Fuzzy System, the weight of clothes put inside it for washing is uncertain but based on weight measured by sensors and the water 
level chosen, it decides total time needed. For low level water, the time estimate is 25 minutes, where approximately weight is between 2000 grams or any nonzero positive
number below that.For medium level water, the time estimate is 35 minutes, where approximately weight is between 2001 grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately weight is above 4000 grams. Assume the capacity of machine is maximum 7000 grams. 
When the weight is zero, time needed is 0 minutes. If the weight exceeds maximum weight limit, then, print “OVERLOADED”, and for all negative weights, the output is “INVALID INPUT”.
Sample Input-1: 2000, L
Sample Output-1: Time Estimated: 25 minutes
Input should be in the form of integer value. 
Output must have the following format: Time Estimated: NN Minutes
'''

def fuzzy_system(weight, water_level):
    if weight < 0:
        print("INVALID INPUT")
    elif weight == 0:
        print("Time Estimated: 0 minutes")
    elif weight > 7000:
        print("OVERLOADED")
    elif weight <= 2000 and water_level == 'L':
        print("Time Estimated: 25 minutes")
    elif weight <= 4000 and water_level == 'M':
        print("Time Estimated: 35 minutes")
    elif weight <= 7000 and water_level == 'H':
        print("Time Estimated: 45 minutes")
    else:
        print("INVALID INPUT")

weight = int(input())
water_level = input().strip().upper()

fuzzy_system(weight, water_level)



    
         
        
    
