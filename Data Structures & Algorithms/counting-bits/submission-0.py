class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n+1):
            bin_str = bin(i)
            res = 0
            for j in range(2, len(bin_str)):
                res += int(bin_str[j])
            output.append(res)
        
        return output
