class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsum = []
        output = []

        def dfs(i, total):
            if total == target:
                output.append(subsum.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            subsum.append(nums[i])
            dfs(i, total+nums[i])
            subsum.pop()
            dfs(i+1, total)
        
        dfs(0,0)
        return output