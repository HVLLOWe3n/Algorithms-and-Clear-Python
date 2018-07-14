#
# Решето эратосфена
#
digits = list()
p = 2

for i in range(1, 121):
    digits.append(i)


for i in digits:
    if i % p == 0:
        digits.remove(i)


