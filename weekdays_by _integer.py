day_number = int(input("Enter a number (1-7): "))
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if (1 <= day_number <= 7):
    print("The day is:", weekdays[day_number - 1])  
else:
    print("Invalid input! Enter a number between 1 and 7.")
