#
# Code for learn
# What is String in Python
# Author @RomanDemyanchuk (HVLLOWe3n)
#


s = 'This is simple string'
s.split()

# Doubles string
print('x3 ' * 3)

# Concatenation
print('Hello ' + 'World')

# string to bytes
print(b'String')

#
# slices [0:n-1:0]
# [first, length, step]
#
print(s[0:5])
print(s[1:5])
print(s[::-1])
print(s[::2])

# any string when changing this is an new string
# example

print('before: ', id(s), s)
s = s[0] + 'F' + s[1:]
print('after: ', id(s), s)

#
# find
#
print(s.find('s'))
# find('str', [start], [end])
print(s.find('s', 0, 3))

# is lower case?
print(s.islower())

# is upper?
print(s.isupper())

# string is contains space or literals
print(s.isspace())

# capitalize string  -> String (first symbol is Upper other lower)
# good function for names or surnames
print(s.capitalize())

print(s.format())

s1 = s

print(s1, id(s1))
print(s, id(s))

s1 += ' Yeah'

print(s1.split('is'))
print(s)
