def find_triplet_with_sum(arr, target_sum):
    # Get the length of the input list
    n = len(arr)
    
    # Iterate through all possible indices for the first element of the triplet
    for i in range(n - 2):
        # Iterate through all possible indices for the second element of the triplet
        for j in range(i + 1, n - 1):
            # Iterate through all possible indices for the third element of the triplet
            for k in range(j + 1, n):
                # Check if the sum of the triplet (arr[i], arr[j], arr[k]) equals the target sum
                if arr[i] + arr[j] + arr[k] == target_sum:
                    # If the sum matches, return the triplet
                    return [arr[i], arr[j], arr[k]]
    
    # If no triplet with the desired sum is found, return None
    return None
# Test the function
arr = [10, 20, 30, 9]
target_sum = 59
result = find_triplet_with_sum(arr, target_sum)
if result:
    print("Triplet with sum", target_sum, ":", result)
else:
    print("No triplet found with sum", target_sum)