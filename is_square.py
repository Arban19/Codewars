def is_square(n):
    if n < 0:
        return False
    else:
        square_root = int(n**0.5)
        return square_root**2 == n
