def sum_of_first_and_last_digits(number):
    # Find the first digit
    first_digit = number
    while first_digit >= 10:
        first_digit //= 10
    
    # Find the last digit
    last_digit = number % 10
    
    # Calculate the sum
    digit_sum = first_digit + last_digit
    
    return digit_sum

# Test the function
number = int(123456)
result = sum_of_first_and_last_digits(number)
print("Sum of the first and last digits:", result)
