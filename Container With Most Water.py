from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while left < right:

            minH = min(heights[left], heights[right])
            maxArea = max(maxArea, minH * (right - left))

            if heights[left] < heights[right]:
                left += 1
                continue
            if heights[left] > heights[right]:
                right -= 1
                continue

            left += 1
            right -= 1

        return maxArea


print(Solution().maxArea([1, 7, 2, 5, 4, 7, 3, 6]))
print(Solution().maxArea([2,2,2]))
