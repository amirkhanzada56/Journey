# Practice Task

# Palindrome Checker

word = input("Enter your word: ")

# Remove Case Sensitivity
word_lower = word.lower()

# check Palindrome
if word_lower == word_lower[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")