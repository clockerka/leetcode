def two_sum(nums, target):
    prev_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[num] = i
    return []