class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    

    def helper(self, nums):
        cur = 0
        prev = 0

        for n in nums:
            prev, cur = cur, max(cur, prev + n)
        
        return cur