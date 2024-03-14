def first_non_repeating(nums):
    # Create a dictionary to store the count of each number
    counts = {}
    
    # Iterate through the list and count occurrences of each number
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if counts[num] == 1:
            return num
    
    # If no non-repeating element found, return None
    return None

# Example list
nums = [10, 501, 22, 37, 100, 999, 87, 351]

# Call the function to find the first non-repeating element
result = first_non_repeating(nums)

# Check if a non-repeating element was found and print the result
if result is not None:
    print("First non-repeating element:", result)
else:
    print("No non-repeating element found.")
