#Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward.

n = '3133'

class Solution:
    def isPalindrome(self, x):  
        return str(x) == str(x)[::-1]

obj = Solution()

print(obj.ifpalindrom(n))



