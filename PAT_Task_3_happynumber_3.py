def is_happy(num):
    # Initialize an empty set to keep track of numbers encountered
    seen = set()
    
    # Keep looping until num equals 1 (a happy number) or num is already seen
    while num != 1 and num not in seen:
        # Add num to the set of seen numbers
        seen.add(num)
        
        # Calculate the sum of squares of digits of num
        num = sum(int(digit) ** 2 for digit in str(num))
    
    # If num equals 1, it's a happy number; otherwise, it's not
    return num == 1
def count_happy_numbers(numbers):
    # Initialize a counter for happy numbers
    count = 0
    
    # Iterate through each number in the list
    for num in numbers:
        # Check if the number is happy using is_happy function
        if is_happy(num):
            # If the number is happy, increment the counter
            count += 1
    
    # Return the count of happy numbers
    return count
# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Count happy numbers
happy_count = count_happy_numbers(numbers)

# Print the count of happy numbers
print("Number of happy numbers in the list:", happy_count)
