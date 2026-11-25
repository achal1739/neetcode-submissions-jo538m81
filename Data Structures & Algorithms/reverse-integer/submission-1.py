class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        
        s = str(abs(x))
        arr = []

        for i in range(len(s)-1, -1, -1):
            arr.append(s[i])
        
        output = int("".join(arr)) * sign
        if -2**31 <= output <= 2**31-1:
            return output
        else:
            return 0

        
