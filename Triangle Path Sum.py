class Solution:
    def solve(self, row, i, triangle, dp):
        n = len(triangle) - 1

        if n == row:
            return triangle[n][i]

        if dp[row][i] != -1:
            return dp[row][i]

        dp[row][i] = (
            min(
                self.solve(row + 1, i, triangle, dp),
                self.solve(row + 1, i + 1, triangle, dp),
            )
            + triangle[row][i]
        )
        return dp[row][i]

    def minPathSum(self, triangle):
        m = len(triangle[-1])
        dp = [[-1] * m for _ in range(m)]
        return self.solve(0, 0, triangle, dp)


print(Solution().minPathSum([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(Solution().minPathSum([[10]]))
