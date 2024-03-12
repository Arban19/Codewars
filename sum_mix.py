"""
Given an array of integers as strings and numbers,
return the sum of the array values as if all were numbers.

Return your answer as a number.

"""

sum_mix = lambda arr: sum(int(x) for x in arr)
