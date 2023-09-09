def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

try:
    user_input = int(input("Enter a year: "))
    if user_input > 0:
        if is_leap_year(user_input):
            print(f"{user_input} is a leap year.")
        else:
            print(f"{user_input} is not a leap year.")
    else:
        print("Please enter a positive year.")
except ValueError:
    print("Invalid input. Please enter a valid year.")
