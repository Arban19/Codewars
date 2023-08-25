def stringy(size):
    output = ""
    for i in range(size):
        output += "1" if i%2 == 0 else "0"

    return output

z = stringy(5)
print(z)
