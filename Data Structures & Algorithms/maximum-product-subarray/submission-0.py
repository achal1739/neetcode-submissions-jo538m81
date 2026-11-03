class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums)
        cur_min = 1
        cur_max = 1

        for n in nums:
            if n == 0:
                cur_min = 1
                cur_max = 1
                continue
            
            temp = n * cur_max
            cur_max = max(temp, n * cur_min, n)
            cur_min = min(temp, n*cur_min, n)
            output = max(output, cur_max)
        
        return output