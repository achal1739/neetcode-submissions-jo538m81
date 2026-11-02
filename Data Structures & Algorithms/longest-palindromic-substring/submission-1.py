class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        res = ""

        for i in range(len(s)):
            left = right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > length:
                    length = right-left+1
                    res = s[left:right+1]
                left -= 1
                right += 1
            
            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > length:
                    length = right-left+1
                    res = s[left:right+1]
                left -= 1
                right += 1
        return res