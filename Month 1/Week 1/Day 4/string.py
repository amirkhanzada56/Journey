# String

str = "Python"

# Indexing

"""
Positve start with 0
Negative start with -1
"""

text = "Python"
print(str[1])      # y
print(str[5])      # n
print(str[-1])     # n

# Slicing

text = "Python"

print(str[0:3])        # Pyt
print(str[:3])         # Pyt
print(str[4:6])        # on
print(str[4:])         # on
print(str[-3:-1])      # ho
print(str[0::2])       # Pto
print(str[::-1])       # nohtyP

# Methods

# String Method

msg = "Hello World"

print(len(msg))                     # 11
print(msg.lower())                  # hello world
print(msg.upper())                  # HELLO WORLD
print(msg.replace("Hello", "Hi"))   # Hi World
