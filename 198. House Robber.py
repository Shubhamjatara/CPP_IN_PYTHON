from typing import List


class Solution:
    def solve(self, arr, n, dp):

        if n < 0:
            return 0

        if n == 0:
            return arr[0]

        if dp[n] != -1:
            return dp[n]

        choose = self.solve(arr, n - 2, dp) + arr[n]
        notChoose = self.solve(arr, n - 1, dp)
        dp[n] = max(choose, notChoose)

        return dp[n]

    def rob(self, nums: List[int]) -> int:

        # top down

        """n = len(nums)
        dp = [-1] * n
        return self.solve(nums, n - 1, dp)"""

        # bottomUp
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = nums[0]
        for i in range(1, n + 1, 1):
            choose = 0
            if (i - 2) >= 0:
                choose = dp[i - 2]

            if i < n:
                choose += nums[i]

            notChoose = dp[i - 1]
            dp[i] = max(choose, notChoose)

        return dp[n]


print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([2, 7, 9, 3, 1]))
print(Solution().rob([2, 1, 1, 2]))
