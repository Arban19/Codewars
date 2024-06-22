"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""

def xo(s):
    return s.lower().count("x") == s.lower().count("o")

def xo(s):
    n_s = [char.lower() for char in s]
    return n_s.count("x") == n_s.count("o")

def xo(s):
    n_s = list(s.lower())
    if "x" or "o" in n_s:
        if n_s.count("x") == n_s.count("o"):
            return True
        else:
            return False
    return True
