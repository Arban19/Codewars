""" In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer. """

def square_digits(num):
    y = []
    for n in str(num):
        y.append(str(int(n)**2))
        z = ""
        for char in y:
            z = "".join(y)
    return z

def square_digits(num):
    return int(''.join(str(int(n)**2) for n in str(num)))

def square_and_str(x):
    return str(x**2)

def square_digits(num):
    digits = map(int, str(num))
    squared_digits = map(square_and_str, digits)
    output = "".join(squared_digits)
    return output

assert square_digits(9119) == "811181"
assert  square_digits(765) == "493625"
