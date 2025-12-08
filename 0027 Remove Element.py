def remove_element(nums, val):
    memboy = 0
    memjoy = len(nums) - 1
    while memboy <= memjoy:
        if nums[memboy] == val:
            nums[memboy] = nums[memjoy]
            memjoy -= 1
        else:
           memboy += 1
    return memboy