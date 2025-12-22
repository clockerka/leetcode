def prefixes_div_by_5(nums):
    otvet = []
    seychas = 0
    for bit in nums:
        seychas = (seychas * 2 + bit) % 5
        otvet.append(seychas == 0)
    return otvet