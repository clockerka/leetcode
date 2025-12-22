def is_happy(n):
    mnozhestvo = set()
    while n != 1 and n not in mnozhestvo:
        mnozhestvo.add(n)
        summa_kvadratov = 0
        while n > 0:
            posledneye_chislo = n % 10
            summa_kvadratov += posledneye_chislo ** 2
            n = n // 10
        n = summa_kvadratov
    return n == 1