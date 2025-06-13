# Function to check if a number is an Armstrong number
def is_armstrong(n):
    original = n
    result = 0
    num_digits = len(str(n))
    
    while n > 0:
        digit = n % 10
        result += digit ** num_digits
        n = n // 10
    
    if result == original:
        return True
    else:
        return False

# Function to check if a number is a Palindrome
def is_palindrome(n):
    original = str(n)
    reversed_num = ''
    
    i = len(original) - 1
    while i >= 0:
        reversed_num += original[i]
        i -= 1

    if original == reversed_num:
        return True
    else:
        return False

# Main part of the program
number = int(input("Enter a number: "))

# Check Armstrong
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is NOT an Armstrong number.")

# Check Palindrome
if is_palindrome(number):
    print(f"{number} is a Palindrome.")
else:
    print(f"{number} is NOT a Palindrome.")
