import random
spisochek = [random.randint(0, 100) for _ in range(100)]
print(spisochek, " - вот ваш список")
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
    skolko_sdvig1 = skolko_sdvig()
    kuda_idem1 = kuda_idem()
    resultat = sam_sdvig(spisochek, skolko_sdvig1, kuda_idem1)
    print("результат циклического сдвига: \n", resultat)
if __name__ == "__main__":
    osnovnaya_funcia()