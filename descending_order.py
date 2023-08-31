def descending_order(numbers):
    sorted_list = sorted(str(numbers), reverse=True)
    return int("".join(sorted_list))
