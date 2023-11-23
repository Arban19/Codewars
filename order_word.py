""" Given a string, you need to write a method that order every letter in this string in ascending order.

Also, you should validate that the given string is not empty or null. If so, the method should return:

"Invalid String!"
Notes
• the given string can be lowercase and uppercase.
• the string could include spaces or other special characters like '# ! or ,'. Sort them based on their ASCII codes """

def order_word(s):
    if not isinstance(s,str) or s == "":
        return "Invalid String!"
    else:
        return "".join(sorted(s))


def order_word(s):
    return "".join(sorted(s)) if s else "Invalid String!"
