#seprate odd And even number
#original list data 
list = [10, 501, 22, 37, 100, 999, 87, 351]
#create even number list 
even_numbers = []
#create a odd number List
odd_numbers = []
#Iterate a the list using for loop
for num in list:
    if num % 2 == 0:# if num /2 we get 0 remainder is even number 
        even_numbers.append(num)# each itration time even number is apprnd to even_numbers variable
        
    else:# other wise is odd number 
        odd_numbers.append(num)
        
# finall print the even and odd number 
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
