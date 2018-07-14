#
# Code for learn
# What is List in Python
# Author @RomanDemyanchuk (HVLLOWe3n)
#

list_one = list('this is list')
print(list_one)

list_two = list_one     # this is not copy!
list_three = [1, 'list', list_two]
print(list_three)

list_three += list_three
print(list_three)


list_four = ['list', 'list_two']

print(list_four.pop(1))
print(list_four)


new_list = [1, 2, 3, 4]
new_copy_list = new_list.copy()

print(new_list, id(new_list))
print(new_copy_list, id(new_copy_list))

new_list = [4, 3, 2, 1]
new_list.sort()

new_list.remove(4)
new_list.append(4)
new_list.insert(0, 7)

print(new_list)
print(new_list.reverse())