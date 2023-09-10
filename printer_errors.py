def printer_error(s):
    error = 0
    for char in s.lower():
        if char not in "abcdefghijklm":
            error += 1
    return f"{error}/{len(s)}"


def printer_error(s):
    allowed_chars = "abcdefghijklm"
    error_count = sum(1 for char in s if char not in allowed_chars)
    return f"{error_count}/{len(s)}"
