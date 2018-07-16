#
# Problem 5 - max number of palindrome 3 - th:
# problem5.py
# Author code: @RomanDemyanchuk (HVLLOWe3n)
#


result = 0      # Result variable for loops cycle
palindrome = 0  # Min and then Max Number palindrome

for j in range(0, 1000):

    for i in range(0, 1000):
        result = str(j * i)

        if result[::-1] == result:

            if int(palindrome) < int(result):
                palindrome = result

print(palindrome)



