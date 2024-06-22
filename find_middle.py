"""
Given a string of characters, I want the function findMiddle()/find_middle()
to return the middle number in the product of each digit in the string.

Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.

Not all strings will contain digits. In this case and the case for any non-strings, return -1.

If the product has an even number of digits, return the middle two digits

Example: 1563 -> 56

NOTE: Remove leading zeros if product is even and the first digit of the two is a zero. Example 2016 -> 1

"""
from functools import reduce

def get_middle(s):
    s = str(s)
    mid = len(s) // 2
    return s[mid] if len(s) % 2 != 0 else s[mid - 1 : mid + 1]

def find_middle(st):
    if not isinstance(st,str):
        return -1

    digits = [int(c) for c in st if c.isdigit()]
    if digits:
        product = reduce(lambda x, y: x*y, digits, 1)
        if product == 0:
            return 0
        elif product % 2 == 0 and str(product)[0] == "0":
            return "".join(str(product).lstrip("0"))
        else:
            return int(get_middle(product))
    return -1
