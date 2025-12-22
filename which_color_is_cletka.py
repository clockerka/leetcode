bukva_lol = input("введите букву клетки\n")
if bukva_lol.isnumeric():
    print("нужно было ввести букву. теперь программа выключается. до свидания.")
    exit()
else:
    bukva = bukva_lol.lower()
    bukvocifra = 0
    if bukva == "a":
        bukvocifra = 1
    elif bukva == "b":
        bukvocifra = 2
    elif bukva == "c":
        bukvocifra = 3
    elif bukva == "d":
        bukvocifra = 4
    elif bukva == "e":
        bukvocifra = 5
    elif bukva == "f":
      bukvocifra = 6
    elif bukva == "g":
        bukvocifra = 7
    elif bukva == "h":
        bukvocifra = 8
    else:
        print("нужно было ввести букву от A до H, чтобы узнать, какого цвета клетка. теперь программа выключается. до свидания.")
        exit()
cifra_lol = input("введите цифру клетки\n")
if cifra_lol.isnumeric():
    cifra = int(cifra_lol)
    if cifra < 1 or cifra > 8:
        print("нужно было ввести цифру от 1 до 8, чтобы узнать, какого цвета клетка. теперь программа выключается. до свидания.")
        exit()
    if cifra % 2 == 0 and bukvocifra % 2 == 0:
        print("клетка черная")
    elif cifra % 2 != 0 and bukvocifra % 2 != 0:
        print("клетка черная")
    else:
        print("клетка белая")
else:
    print("нужно было ввести цифру от 1 до 8, чтобы узнать, какого цвета клетка. теперь программа выключается. до свидания.")
    exit()