#
# Code for learn
# What is Set in Python
# Author @RomanDemyanchuk (HVLLOWe3n)
#
s = set('Hello')

print(s)
print(s.remove('l'))
print(s)

s1 = set('World!')

#
# Обьеденение set - а!
#
s1.union(s)

print(s1)

new_set = set('Hello')
other = set('Hellos')

print(new_set.issubset(other))       # <=
print(new_set.issuperset(other))     # >=
print(new_set == other)
print(new_set is other)


# frozenset - тот же set но как tuple!
fs = frozenset('Hello')

print(fs == new_set)
