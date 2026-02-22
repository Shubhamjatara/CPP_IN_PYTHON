from typing import List


class Solution:
    def nse(self, arr: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            ans[i] = len(arr) if not stack else stack[-1]
            stack.append(i)

        return ans

    def pse(self, arr: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            ans[i] = -1 if not stack else stack[-1]

            stack.append(i)

        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        nse = self.nse(heights)
        pse = self.pse(heights)
        area = 0

        n = len(heights)

        for i in range(n):
            left = pse[i]+1
            right = nse[i]-1
            width = (right-left)+1
            area = max(heights[i] * width, area)

        return area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([2, 4]))
print(Solution().largestRectangleArea([2, 2]))
print(Solution().largestRectangleArea([1, 2, 2]))
print(Solution().largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0]))
