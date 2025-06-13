def factorial(n):
    # Basic concept: input validation
    if not isinstance(n, int) or n < 0:
        print("Please enter a non-negative integer.")
        return None

    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

# Example usage
num = int(input("Enter a number: "))
result = factorial(num)
if result is not None:
    print(f"Factorial of {num} is {result}")