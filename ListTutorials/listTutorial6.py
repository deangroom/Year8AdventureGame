# Creating a list
my_list = [1, 2, 3, 4, 5]

# List methods
print(my_list.count(5))  # Output: 1
print(my_list.index(8))  # Output: 2

# Concatenating lists
new_list = my_list + [7, 8]
print(new_list)  # Output: [1, 10, 8, 9, 5, 6, 7, 8]

# Checking for membership
print(5 in my_list)  # Output: True

# copying lists
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 10, 8, 9, 5, 6]

#check if copied list is same as my_list
print(copied_list is my_list)  # Output: False

