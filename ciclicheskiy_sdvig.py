def sdvig_vpravo(spisok):
    posledniy = spisok[-1]
    for i in range(len(spisok) - 1, 0, -1):
        spisok[i] = spisok[i - 1]
    spisok[0] = posledniy
    return spisok
def sdvig_vlevo(spisok):
    perviy = spisok[0]
    for i in range(0, len(spisok) - 1):
        spisok[i] = spisok[i + 1]
    spisok[-1] = perviy
    return spisok
spisokdfdv = [1, 2, 3, 4, 5]
dshbhidbv = sdvig_vlevo(spisokdfdv)
print(dshbhidbv)