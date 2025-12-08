def is_palindrome(x):
    xstringi = str(x)
    perevernul = xstringi[::-1]
    if xstringi == perevernul:
        return True
    else:
        return False