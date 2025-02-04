#You have a year in mind, and your task is to write a program that determines if this year is a leap year. Can you figure out if it has an extra day in February?

year = int(input("Enter a year: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

total_days = 366 if is_leap else 365
feb_days = 29 if is_leap else 28

print(f"{year} is a leap year with {total_days} days, and February has {feb_days} days." if is_leap
      else f"{year} is not a leap year, it has {total_days} days, and February has {feb_days} days.")
