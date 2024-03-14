def sub_list_with_sum_zero(lst):
    # Iterate through all possible sub-list starting indices
    for i in range(len(lst)):
        current_sum = 0
        # Iterate through all possible sub-list lengths starting from i
        for j in range(i, len(lst)):
            current_sum += lst[j]
            # If sum equals zero, return True
            if current_sum == 0:
                return True
    # If no such sub-list found, return False
    return False

#  Test the function
my_list = [4, 2, -3, 1, 6]
if sub_list_with_sum_zero(my_list):
    print("There is a sub-list with sum equal to zero.")
else:
    print("There is no sub-list with sum equal to zero.")
