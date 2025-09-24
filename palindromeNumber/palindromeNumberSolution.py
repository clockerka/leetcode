class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstringi = str(x)
        perevernul = xstringi[::-1]
        if xstringi == perevernul:
            return True
        else:
            return False