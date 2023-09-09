def is_isogram(word):
    set = ""
    for char in word.lower():
        if char in set:
            return False
        else:
            set += char
    return True
