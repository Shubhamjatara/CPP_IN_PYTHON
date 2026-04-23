from typing import List


class Solution:
    def solve(self, row, col, mat, dp):
        lastIndexRow = len(mat) - 1
        lastIndexCol = len(mat[0]) - 1

        if (lastIndexRow < row) or (lastIndexCol < col) or mat[row][col] == 1:
            return 0

        if dp[row][col] != -1:
            return dp[row][col]

        if (row == lastIndexRow) and (col == lastIndexCol):
            return 1
        dp[row][col] = self.solve(row, col + 1, mat, dp) + self.solve(
            row + 1, col, mat, dp
        )
        return dp[row][col]

    """ 
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
         dp = [[-1] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
         return self.solve(0,0,obstacleGrid,dp) """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp[0][0] = 0
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                
                if obstacleGrid[row][col] == 1:
                    continue
                
                if (row == m - 1) and (col == n - 1) and obstacleGrid[row][col]!=1:
                    dp[m - 1][n - 1] = 1
                    continue

                up = (
                    dp[row + 1][col]
                    if ((row + 1 < m) and (obstacleGrid[row + 1][col] != 1))
                    else 0
                )
                left = (
                    dp[row][col + 1]
                    if ((col + 1 < n) and (obstacleGrid[row][col + 1] != 1))
                    else 0
                )

                dp[row][col] = up + left
                
        return dp[0][0]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(Solution().uniquePathsWithObstacles([[1]]))
print(Solution().uniquePathsWithObstacles([[1,0]]))

