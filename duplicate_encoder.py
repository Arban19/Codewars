"""
The goal of this exercise is to convert a string to a new string
where each character in the new string is "(" if that character
appears only once in the original string, or ")" if that character
appears more than once in the original string.

Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

"""

def duplicate_encode(word):
    word_lower = word.lower()
    char_count = {char: word_lower.count(char) for char in set(word_lower)}
    new_word = ''.join([')' if char_count[char] > 1 else '(' for char in word_lower])
    return new_word

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
