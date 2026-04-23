class Solution:
    def solve(self, i, k, mat, dp):
        if i >= len(mat):
            return 0

        if (k != -1) and dp[i][k] != -1:
            return dp[i][k]

        max_val = 0
        for j in range(3):

            if k != j:
                max_val = max(max_val, self.solve(i + 1, j, mat, dp) + mat[i][j])

        if k != -1:
            dp[i][k] = max_val

        return max_val

    def maximumPoints(self, mat):
        dp = [[-1] * 3 for _ in range(len(mat))]

        return self.solve(0, -1, mat, dp)
       

print(Solution().maximumPoints([[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
print(Solution().maximumPoints([[1, 1, 1], [2, 2, 2], [3, 3, 3]]))
print(Solution().maximumPoints([[4, 2, 6]]))
 