import random
spisok = [random.randint(-100, 100) for y in range(50)]
print(spisok, " - вот ваш список")
bolschee_po_moduly = 0
result = 0
for i in spisok:
    if i % 2 == 0 and i % 3 != 0:
        if i >= 0:
            modul = i
        else:
            modul = -1 * i
        if modul > bolschee_po_moduly:
            bolschee_po_moduly = modul
            result = i
print("максимально число по модулю: ", result, "(модуль: ", bolschee_po_moduly, ")")