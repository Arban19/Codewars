def friend(names):
    output = []
    for name in names:
        if len(name) == 4:
            output.append(name)
    return output


print(friend(["Jason","mark","steve","kill","neat"]))
