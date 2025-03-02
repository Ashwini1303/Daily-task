#Program to calculate hours, minutes and seconds for a given input days

def calculate_days(days):
    hours = days * 24
    minutes = hours * 60  
    seconds = minutes * 60 
    return hours, minutes, seconds  
days = int(input("Enter the number of days: "))
hours, minutes, seconds = calculate_days(days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

    
