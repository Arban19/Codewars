def distinct(seq):
    result = []
    output = set()

    for num in seq:
        if num not in output:
            result.append(num)
            output.add(num)
    return result
