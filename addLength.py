def add_length(str_):
    result = []
    for char in str_.split():
        length = len(char)
        result.append(f"{char} {length}")
    return result
