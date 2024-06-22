def find_uniq(arr):
    unique_occurences = {}
    for item in arr:
        if item in unique_occurences:
            unique_occurences[item] += 1
        else:
            unique_occurences[item] = 1

    for key, value in unique_occurences.items():
        if value == 1:
            return key



assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
