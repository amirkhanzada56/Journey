# Practice Task: Student Marks Dictionary

marks = {}

# Adding Data
marks["english"] = int(input("Enter English marks: "))
marks["math"] = int(input("Enter Math marks: "))
marks["chemistry"] = int(input("Enter Chemistry marks: "))

print("\nStudent Marks")
for subject, mark in marks.items():
    print(subject, ":", mark)


