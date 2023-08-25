def disemvowel(strings_):
    vowels = "AEIOUaeiou"
    return "".join([char for char in strings_ if char not in vowels])

print(disemvowel("Drunk fifteen in the EDM scene"))
