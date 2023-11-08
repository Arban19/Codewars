def is_leap_year(year):
    if year%400 == 0 or year%4 == 0:
        return True
    elif year%100 == 0:
        return False
    else:
        return False

print(is_leap_year(2100))
