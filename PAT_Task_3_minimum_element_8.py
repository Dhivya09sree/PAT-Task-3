# Define a function to find the minimum element in a sorted list
def find_minimum_sorted_list(input_list):
    # Check if the list is empty
    if not input_list:
        return None  # Return None if the list is empty
    
    # Return the first element of the list, which is the minimum element
    return input_list[0]


# Test the function
# Create a sorted list of numbers
sorted_list = [1, 2, 3, 4, 5]

# Call the function with the sorted list
minimum_element = find_minimum_sorted_list(sorted_list)

# Print the minimum element found
print("Minimum element in the sorted list:", minimum_element)
