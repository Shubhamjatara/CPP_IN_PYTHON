# brute force
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        k = 0
        for i in range(len(heights)):
            mini = heights[i]
            area = max(area, 1 * mini)
            for j in range(i, len(heights), 1):
                width = (j - i) + 1
                if heights[j] < mini:
                    break
                area = max(area, width * mini)

        while k < len(heights):
            most_min = heights[k]
            for l in range(k, len(heights), 1):
                if heights[l] != 0:
                    most_min = min(most_min, heights[l])
                    area = max(area, ((l - k) + 1) * most_min)
                else:

                    break
            k += 1

        return area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([2, 4]))
print(Solution().largestRectangleArea([2, 1, 2]))
print(Solution().largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0]))
