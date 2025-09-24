class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        chastota = Counter(nums)
        max_chastota = max(chastota.values())
        total = sum(count for count in chastota.values() if count == max_chastota)
        return total