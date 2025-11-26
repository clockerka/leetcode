import random
def poluchit_spisok():
    popytochechki = 3
    while popytochechki > 0:
        vybor_veka = input("Сгенерировать список рандомно (автоматически) или ввести самому? r - если хотите, чтобы список сгенерировался автоматически, m - если хотите сами его ввести: \n\n").strip().lower()
        if vybor_veka == "r":
            try:
                razmer = int(input("введите размер списка (не более 100): \n\n"))
                if razmer > 100:
                    print("вы не соблюдали правила. программа выключена. в следующий раз соблюдайте правила.")
                    exit()
                return [random.randint(0, 100) for _ in range(razmer)]
            except ValueError:
                print("вы не соблюдали правила. программа выключена. в следующий раз соблюдайте правила.")
                exit()
        elif vybor_veka == "m":
            print("введите элементы списка через пробел и нажмите enter (в списке может быть не более 100 элементов, все - числовые): \n\n")
            try:
                spisok = list(map(int, input().split()))
                if len(spisok) > 100:
                    print("вы не соблюдали правила. программа выключена. в следующий раз соблюдайте правила.")
                    exit()
                print(spisok, " - ваш список\n\n")
                return spisok
            except ValueError:
                print("вы не соблюдали правила. программа выключена. в следующий раз соблюдайте правила.")
                exit()
        else:
            popytochechki -= 1
            print(f"ошибка ввода. осталось попыток: {popytochechki}\n\n")
    print("вы не соблюдали правила. Программа выключена. в следующий раз соблюдайте правила.")
    exit()
def skolko_sdvig():
    popytki = 3
    while popytki > 0:
        try:
            skolko = int(input("на сколько элементов нужно сделать циклический сдвиг списка? \n\n"))
            return skolko
        except ValueError:
            popytki -= 1
            print(f"введите число. осталось попыток: {popytki}\n\n")
    print("вы не соблюдали правила. программа выключена. в следующий раз соблюдайте правила.")
    exit()
def kuda_idem():
    popytochki = 3
    while popytochki > 0:
        napravleniye = input("куда делать циклический сдвиг? вправо (r) или влево (l): \n\n").strip().lower()
        if napravleniye in ["r", "l"]:
            return napravleniye
        popytochki -= 1
        print(f"введите 'r' для вправо или 'l' для влево. осталось попыток: {popytochki}\n\n")
    print("вы не соблюдали правила. программа выключена. в следующий раз соблюдайте правила.")
    exit()
def sam_sdvig(lst, shift, direction):
    shift %= len(lst)
    if direction == "r":
        return lst[-shift:] + lst[:-shift]
    elif direction == "l":
        return lst[shift:] + lst[:shift]
def osnovnaya_funcia():
    poluchit_spisok1 = poluchit_spisok()
    skolko_sdvig1 = skolko_sdvig()
    kuda_idem1 = kuda_idem()
    resultat = sam_sdvig(poluchit_spisok1, skolko_sdvig1, kuda_idem1)
    print("результат циклического сдвига: \n", resultat)
if __name__ == "__main__":
    osnovnaya_funcia()