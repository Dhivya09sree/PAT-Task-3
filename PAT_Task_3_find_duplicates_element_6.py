def find_duplicates(list1, list2, list3):
    # Convert the lists to sets
    set1 = set(list1)
    set2 = set(list2)
    set3 = set(list3)
    
    # Find the intersection of the three sets
    duplicates = set1.intersection(set2, set3)
    
    # Return the set of duplicates
    return duplicates

# Example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 7, 8, 9]
list3 = [3, 4, 8, 10, 11]

# Find duplicates
duplicate_elements = find_duplicates(list1, list2, list3)

if len(duplicate_elements) > 0:
    print("Duplicates found:", duplicate_elements)
else:
    print("No duplicates found.")
