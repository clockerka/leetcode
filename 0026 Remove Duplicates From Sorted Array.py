def remove_duplicates(nums):
    for i in range(0, len(nums) - 1, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i)