def best_friend(text, a, b):
    i = 0
    while i < len(text):
        try:
            char = text[i]
            char_next = text[i + 1]
        except IndexError:
            char_next = " "
        if char == a and char_next != b:
                return False
        i += 1
    return True
