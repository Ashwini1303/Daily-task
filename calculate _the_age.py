#Write a program to calculate age based on input of date, month and year

from datetime import date

def calculate_age(birth_day, birth_month, birth_year):
    today = date.today()
    current_day, current_month, current_year = today.day, today.month, today.year
    age = current_year - birth_year
    if (birth_month > current_month) or (birth_month == current_month and birth_day > current_day):
        age -= 1
    return age

birth_day = int(input("Enter birth day (DD): "))
birth_month = int(input("Enter birth month (MM): "))
birth_year = int(input("Enter birth year (YYYY): "))

age = calculate_age(birth_day, birth_month, birth_year)
print(f"Your age is: {age} years")


