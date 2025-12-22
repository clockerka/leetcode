def max_frequency_elements(nums):
    chastota = Counter(nums)
    max_chastota = max(chastota.values())
    total = sum(count for count in chastota.values() if count == max_chastota)
    return total