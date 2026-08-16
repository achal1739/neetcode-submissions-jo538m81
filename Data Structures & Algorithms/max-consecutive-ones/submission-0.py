class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0

        for i in range(len(nums)):
            counter = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    break
                counter += 1
            output = max(output, counter)
        
        return output 