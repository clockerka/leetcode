def max_area(height):
    i = 0
    j = len(height) - 1
    result = 0
    while i < j:
        seychas = min(height[i], height[j]) * (j - i)
        result = max(result, seychas)
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return result