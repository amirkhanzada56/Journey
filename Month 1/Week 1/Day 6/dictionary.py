# Dictionary

student = {
    "name" : "Amir",
    "age" : 18,
    "marks" : 95
}

# Access
print(student["name"])      # Amir
print(student.get("agee"))  # None
print(student.keys())
print(student.values())

# Add / Update
student.update({"name" : "Fakhir"})
student["grade"] = "A"
print(student)

# Remove
student.pop("age")
print(student)

# Item in tuple
print(student.items())
