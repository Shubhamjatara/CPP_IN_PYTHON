class Solution:
    def solve(self, row, col, m, n, dp):
        lastIndexRow = m - 1
        lastIndexCol = n - 1

        if (lastIndexRow < row) or (lastIndexCol < col):
            return 0

        if dp[row][col] != -1:
            return dp[row][col]

        if (row == lastIndexRow) and (col == lastIndexCol):
            return 1
        dp[row][col] = self.solve(row, col + 1, m, n, dp) + self.solve(
            row + 1, col, m, n, dp
        )
        return dp[row][col]

        """     def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        return self.solve(0, 0, m, n, dp) """

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n) for _ in range(m)]
        dp[m - 1][n - 1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):

                if (m - 1 == row) and (n - 1 == col):
                    continue

                right = dp[row][col + 1] if col + 1 < n else 0
                down = dp[row + 1][col] if row + 1 < m else 0

                dp[row][col] = right + down

        return dp[0][0]


print(Solution().uniquePaths(3, 7))
""" print(Solution().uniquePaths(3, 2)) """
