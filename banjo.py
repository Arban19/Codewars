def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return f"{name.title()} plays banjo"
    else:
        return f"{name.title()} does not play banjo"

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
