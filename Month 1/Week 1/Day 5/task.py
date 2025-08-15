# Grocery List Program

grocery = []

# Add items
grocery.append(input("Enter first item: "))
grocery.append(input("Enter second item: "))
grocery.append(input("Enter third item: "))

print("\n Your Glocery List")
for item in grocery:
    print("_", item)