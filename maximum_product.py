"""
Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array. 
Note that the array size is at least 2 and consists a mixture of positive, negative integers and also zeroes.

Examples
[1, 2, 3] returns 6 because the maximum product is obtained from multiplying 

"""

def adjacent_element_product(array):
    product_list = []
    for i in range(len(array) - 1):
        product_list.append(array[i]*array[i+1])
    
    return print(max(product_list))
