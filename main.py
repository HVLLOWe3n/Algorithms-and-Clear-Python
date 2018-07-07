import random

from Bubble_Sort_Algorithm import bubble_sort
from Fibonachi_Digits_Algorithm import fibonach_digits

# Standart Types of Python
a = 3                   # a - class integer
new_a = 3.1415          # new_a - class float
s = 'String'            # s - class string
b = False               # b - class bool

print(type(a))          # type - is a function for identify type of variable
print(type(new_a))
print(type(s))
print(type(b))

# None
none_variable = None
print(type(none_variable))      # None is object to

if none_variable is None:
    print('none_variable is None')

else:
    print('none_variable is not None')

#
# Digits
#
a = 12
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

print(a // b)           # получение целой части от деления
print(a ** b)           # возведение в степень
print(-a)

print(abs(-a))          # модуль
print(divmod(a, b))     # Пара (x // y, x % y)

print(3 ** 150)

# int.to_bytes(length, byteorder, *, signed=False) - возвращает строку байтов, представляющих это число.
a = (1024).to_bytes(2, byteorder='big')
print(a, type(a))

# a = input('Press you name: ')
#
# str_name = 'Hello, {0}!'.format(a)
# print(str_name)

print(3 // 4, 4 + False - True)
print((2 + 3) * 4, 2 + (3 * 4))


time = input('Input you time right now: ')

try:
    if int(time) <= 12:
        print('Good Morning!')

    elif (int(time) > 12) and (int(time) < 16):
        print('Good Day!')

    else:
        print('Good Evening!')

except ValueError:
    print('You must input integer value!')

running = True

# while running:
#     try:
#         my_val = input('Input you value from 1 .. 6: ')
#
#         if my_val == random.randrange(6):
#             print('Success, congratulations!')
#
#             break
#         else:
#             print('None right, try again :)')
#     except ValueError:
#         print('You must input you value from 1 .. 6')

# ## loop for ##

for i in range(1, 20):
    print(i)


for i in range(2, 10):

    print(fibonach_digits(i))
