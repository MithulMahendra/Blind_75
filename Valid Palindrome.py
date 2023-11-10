class Solution:
    def isPalindrome(self, s: str) -> bool:
        f_s=""
        s=s.lower()
        for char in s:
            if char.isalnum():
                f_s+=char
        return f_s==f_s[::-1]

#Leetcode Problem : 125
