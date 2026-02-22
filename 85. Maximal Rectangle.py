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

    def findMaxRectangleInHistoGram(self, arr: List[int]) -> int:
        nse = self.nse(arr)
        pse = self.pse(arr)
        area = 0

        n = len(arr)

        for i in range(n):
            left = pse[i] + 1
            right = nse[i] - 1
            width = (right - left) + 1
            area = max(arr[i] * width, area)

        return area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0
        arr = [0] * len(matrix[0])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if arr[col] >= 1 and int(matrix[row][col]) == 0:
                    arr[col] = 0
                else:
                    arr[col] += int(matrix[row][col])
            maxarea = max(maxarea, self.findMaxRectangleInHistoGram(arr))

        return maxarea


print(
    Solution().maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)

print(Solution().maximalRectangle([["0"]]))

print(Solution().maximalRectangle([["1"]]))
