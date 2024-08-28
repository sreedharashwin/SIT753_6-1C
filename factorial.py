# Function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Predefined number
number = 7

# Calculate factorial
result = factorial(number)

# Print result
print(f"The factorial of {number} is {result}")

