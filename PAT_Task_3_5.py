def distribute_mangoes(mangoes, students):
    mangoes.sort()  # Sort the mangoes in ascending order
    bags_assigned = [[] for _ in range(students)]  # Initialize bags for each student

    for mango in mangoes:
        min_bag = min(bags_assigned, key=sum)  # Find the bag with the least mangoes
        min_bag.append(mango)  # Assign the mango to the bag with the least mangoes

    return bags_assigned

# Example usage:
mangoes = [7, 3, 2, 8, 10, 5]
students = 3
result = distribute_mangoes(mangoes, students)
print("Bags assigned to students:", result)
