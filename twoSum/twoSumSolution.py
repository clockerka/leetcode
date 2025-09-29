from typing import List
class Solution:
    def twoSum(self, nomera: List[int], cel: int) -> List[int]:
        pary = [(i, j) for i in range(len(nomera)) for j in range(i + 1, len(nomera))]
        for i, j in pary:
            if nomera[i] + nomera[j] == cel:
                return [i, j]
        return []
