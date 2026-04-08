class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        width = 0
        height = 0
        water = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            water = max(water, (height*width))

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return water