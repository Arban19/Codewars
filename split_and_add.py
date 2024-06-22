"""
Task
You will receive an array as parameter that contains 1 or more integers and a number n.

Here is a little visualization of the process:

Step 1: Split the array in two:

[1, 2, 5, 7, 2, 3, 5, 7, 8]
      /            \
[1, 2, 5, 7]    [2, 3, 5, 7, 8]
Step 2: Put the arrays on top of each other:

   [1, 2, 5, 7]
[2, 3, 5, 7, 8]
Step 3: Add them together:

[2, 4, 7, 12, 15]
Repeat the above steps n times or until there is only one number left, and then return the array.

Example
Input: arr=[4, 2, 5, 3, 2, 5, 7], n=2


Round 1
-------
step 1: [4, 2, 5]  [3, 2, 5, 7]

step 2:    [4, 2, 5]
        [3, 2, 5, 7]

step 3: [3, 6, 7, 12]


Round 2
-------
step 1: [3, 6]  [7, 12]

step 2:  [3,  6]
         [7, 12]

step 3: [10, 18]


Result: [10, 18]


"""

def divide(numbers):
    mid = len(numbers)//2
    return numbers[:mid], numbers[mid:]

def get_value(l1,i):
    try:
        z = l1[i]
    except IndexError:
        z = 0
    return z

def add_elements(list1, list2):
    result = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
             result.append(list1[i] + list2[i])
        return result
    elif len(list1) != len(list2):
        higher = max(len(list1),len(list2))
        for i in range(1, higher + 1):
            result.append(get_value(list1,-i) + get_value(list2,-i))
        result.reverse()
        return result

def split_and_add(numbers, n):
    output = numbers
    rounds = n
    while n > 0 and len(output) > 1:
        a1, a2 = divide(output)
        output = add_elements(a1, a2)
        n -= 1
    return output
