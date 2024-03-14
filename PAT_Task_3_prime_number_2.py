# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num // 2 + 1):  # Loop up to half of num
        if num % i == 0:
            return False
    return True

# Original list data
list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create a list to store prime numbers
prime_numbers = []

# Iterate through the list and check if each number is prime
for num in list:
    if is_prime(num):
        prime_numbers.append(num)

# Finally, print the count of prime numbers and the list of prime numbers
print("Number of prime numbers:", len(prime_numbers))
print("Prime numbers:", prime_numbers)
