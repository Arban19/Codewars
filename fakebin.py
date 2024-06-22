# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    list = ""
    for i in x:
        if int(i) < 5:
            list += "0"
        elif int(i) >= 5:
            list += "1"
    return list

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
