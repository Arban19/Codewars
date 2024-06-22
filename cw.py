def triple_trouble(one, two, three):
    result = ''
    for x, y, z in zip(one, two, three):
        result += x + y + z
    return result

print(triple_trouble('cat', 'dog', 'ape'))
    
