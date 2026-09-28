class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sub = []
        output = []

        def dfs(i, total):
            if total == target:
                output.append(sub.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            sub.append(nums[i])
            dfs(i, total+nums[i])

            sub.pop()
            dfs(i+1, total)
        
        dfs(0,0)
        return output