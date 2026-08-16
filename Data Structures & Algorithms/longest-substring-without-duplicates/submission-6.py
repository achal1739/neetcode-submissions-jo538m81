class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 1
        hashset = set()
        left = 0

        if s == "":
            return 0

        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            output = max(right-left +1, output)
        
        return output 

        

        
        