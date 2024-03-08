# Creating a list
my_list = [1, 2, 3, 4, 5]


# Conditional list comprehension
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]
