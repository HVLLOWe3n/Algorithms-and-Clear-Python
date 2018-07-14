result = 0
palindrome = 0

for j in range(0, 1000):

    for i in range(0, 1000):
        result = str(j * i)

        if result[::-1] == result:

            if palindrome < int(result):
                 palindrome = result
                 print(palindrome)





