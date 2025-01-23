def classify_age_group(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior citizen"

age = int(input("Enter your age: "))
print("Your age group is:", classify_age_group(age))
