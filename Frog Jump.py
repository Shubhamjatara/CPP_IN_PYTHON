class Solution:
    def solve(self, arr, n, dp):
        if dp[n] != -1:
            return dp[n]

        if n == 1:
            return abs(arr[n] - arr[n - 1])
        if n == 0:
            return 0
        dp[n] = min(
            self.solve(arr, n - 1, dp) + abs((arr[n] - arr[n - 1])),
            self.solve(arr, n - 2, dp) + abs(arr[n] - arr[n - 2]),
        )
        return dp[n]

    def minCost(self, height):

        n = len(height)

        if len(height) == 1:
            return 0

        dp = [-1] * (n + 1)

        return self.solve(height, n - 1, dp)


print(Solution().minCost([0,2,5,6,7]))
