def is_valid(s):
    hranilische = []
    vidi_skobok = {')': '(', '}': '{', ']': '['}
    for znak in s:
        if znak in vidi_skobok.values():
            hranilische.append(znak)
        elif znak in vidi_skobok:
            if not hranilische or hranilische[-1] != vidi_skobok[char]:
                return False
            hranilische.pop()
    return not hranilische