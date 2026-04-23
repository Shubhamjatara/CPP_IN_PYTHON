class Solution:
    def solve(self, n, sum, arr, dp):
        if sum == 0:
            return True

        if n < 0:
            return False

        if dp[n][sum]:
            return dp[n][sum]

        choose = False
        if arr[n] <= sum:
            choose = self.solve(n - 1, sum - arr[n], arr, dp)

        notChoose = self.solve(n - 1, sum, arr, dp)
        dp[n][sum] = choose or notChoose
        return dp[n][sum]

    def isSubsetSum(self, arr, sum):
        n = len(arr)
        dp = [[None] * (sum + 1) for _ in range(n)]
        return self.solve(n - 1, sum, arr, dp)


print(Solution().isSubsetSum([3, 34, 4, 12, 5, 2], 9))
print(Solution().isSubsetSum([3, 34, 4, 12, 5, 2], 30))
print(Solution().isSubsetSum([1, 2, 3], 6))
