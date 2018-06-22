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
