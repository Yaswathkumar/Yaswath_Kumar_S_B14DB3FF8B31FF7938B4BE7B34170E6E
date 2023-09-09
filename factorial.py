def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    user_input = int(input("Enter a non-negative integer: "))
    if user_input >= 0:
        result = factorial(user_input)
        print(f"The factorial of {user_input} is {result}.")
    else:
        print("Please enter a non-negative integer.")
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")
