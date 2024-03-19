def find_even_index(arr):
    left, right = 0, 0

    for i in range(len(arr)):
        if i == 0:
            left = 0
            right = sum(arr[1:])
        elif i == (len(arr)-1):
            left = sum(arr[:-1])
            right = 0
        else:
            left = sum(arr[:i])
            right = sum(arr[i+1:])

        if left == right:
            return i
        else:
            continue
    return -1

print(find_even_index([1,2,3,4,3,2,1]))
