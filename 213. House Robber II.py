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
        temp1 = []
        temp2 = []
        n = len(nums)

        if n == 1:
            return nums[0]

        dp1 = [-1] * n
        dp2 = [-1] * n
        for i in range(0, n - 1, 1):
            temp1.append(nums[i])
        for j in range(1, n, 1):
            temp2.append(nums[j])

        return max(
            self.solve(temp1, len(temp1) - 1, dp1),
            self.solve(temp2, len(temp2) - 1, dp2),
        )


print(Solution().rob([2, 3, 2]))
print(Solution().rob([1, 2, 3, 1]))
print(Solution().rob([1, 2, 3]))
print(Solution().rob([1]))
