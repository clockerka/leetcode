def isPalindrome(x):
    return x == x[::-1]
print(isPalindrome("ananana")) # выведет True
print(isPalindrome("ananas")) # выведет False