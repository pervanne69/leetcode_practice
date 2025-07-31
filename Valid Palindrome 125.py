class Solution:
    def isPalindrome(self, s: str) -> bool:
        string1 = [i for i in s.lower() if i.isalnum()]
        return string1 == string1[::-1]