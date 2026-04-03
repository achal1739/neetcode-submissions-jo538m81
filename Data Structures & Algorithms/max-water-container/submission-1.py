class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        height_value = 0
        width = 0
        water = 0

        while left < right:
            height_value = min(heights[right], heights[left])
            width = right - left
            water = max(water, (height_value*width))

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return water