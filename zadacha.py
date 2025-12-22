import random
spisok = [random.randint(-100, 100) for i in range(50)]
print(spisok, " - вот ваш список")
bolschee_po_moduly = 0
result = 0
for chislo in spisok:
    if chislo % 2 == 0 and chislo % 3 != 0:
        if chislo >= 0:
            modul = chislo
        else:
            modul = -1 * chislo
        if modul > bolschee_po_moduly:
            bolschee_po_moduly = modul
            result = chislo
print("максимально число по модулю: ", result, "(модуль: ", bolschee_po_moduly, ")")