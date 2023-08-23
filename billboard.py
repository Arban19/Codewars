def billboard(name, price=30):
    quote = 0
    for units in name:
        quote += price

    return quote
