""" Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers. """


def sorting_key(words):
    for char in words:
        if char.isdigit():
            return int(char)

def order(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key= sorting_key)
    sorted_sentence = " ".join(sorted_words)
    return sorted_sentence


assert order("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est"
assert order("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
assert order("") ==  ""