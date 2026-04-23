from typing import List


class Solution:
    def solve(self, n: int, dp: List[int]) -> int:
        if dp[n] != -1:
            return dp[n]
        if n == 0:
            return 1
        if n < 0:
            return 0

        dp[n] = self.solve(n - 1, dp) + self.solve(n - 2, dp)
        return dp[n]

    def solveByBottomUp(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1, 1):
            if (i - 2) >= 0:
                dp[i] += dp[i - 2]

            dp[i] += dp[i - 1]

        return dp[n]

    def climbStairs(self, n: int) -> int:
        return self.solveByBottomUp(n)
