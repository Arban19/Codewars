""" Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""

def solution(sentence):
    i = 0
    words = []
    for j, char in enumerate(sentence):
        if char.isupper():
            words.append(sentence[i:j])
            i = j
    words.append(sentence[i:])
    result = " ".join(words).strip()
    return result
