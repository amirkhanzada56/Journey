# List in python

# Creating
my_list = ["apple", 15, "Amir", 44.55, 343, False]

# Access Elements
print(my_list[1])           # Access element at index 1 → 15
print(my_list[-1])          # Access last element → False

# Modify Element 
my_list[2] = "cherry"
print(my_list)               # ['apple', 15, 'cherry', 44.55, 343, False]

# Add Elements
my_list.append("orange")     # Append to the end of the list
print(my_list)

my_list.insert(3, 12)        # Insert 12 at index 3
print(my_list)

# Remove Elements
my_list.remove(343)          # Remove the first occurrence of value 343
print(my_list)

my_list.pop(0)               # Remove element at index 0 ('apple')
print(my_list)
