def find_even_index(arr):
    left, right = 0, 0

    for i in range(len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i+1:])

        if left == right:
            return i

    return -1
