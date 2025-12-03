def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    totalno = 0
    prediduschiy_simvol = 0
    for i in reversed(s):
        simvol = roman[i]
        if simvol < prediduschiy_simvol:
            totalno -= simvol
        else:
            totalno += simvol
        prediduschiy_simvol = simvol
    return totalno