# Sets

empty_set = set()

fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)

# Add
fruits.add("mango")

# Remove
# fruits.remove("chair") --> Error if not found
fruits.discard("cherry")     # No error if not fount

print(fruits)
print(type(empty_set), type(fruits))

# Union & Intersection
s1 = {1, 4, 7, 9}
s2 = {6, 5, 7, 11}

print(s1.union(s2))
print(s1.intersection(s2)) 