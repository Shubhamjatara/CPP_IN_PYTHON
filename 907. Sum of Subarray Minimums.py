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

    def sumSubarrayMins(self, arr: List[int]) -> int:
        nse = self.nse(arr)
        pse = self.pse(arr)
        total = 0
        mod = 10**9 + 7
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + left * right * arr[i]) % mod

        return total


print(Solution().sumSubarrayMins([3, 1, 2, 4]))
