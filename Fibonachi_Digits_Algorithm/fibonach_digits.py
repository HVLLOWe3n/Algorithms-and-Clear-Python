#
# Algorithm lessons
# This algorithm --------> Fibonachi Digits
# Author code: @RomanDemyanchuk (HVLLOWe3n)
#


#
# Simple Realise
# without recursion
#
def simple_fibonachi(n):
    if n <= 0 or n <= 1:
        return

    preview = 1
    preview_preview = 1
    result = 0

    for i in range(0, n):

        result = preview_preview + preview
        preview_preview = preview
        preview = result

    return result


#
# Hard realise
# with recursion
#

def recursion_fibonachi():
    pass