from math import floor
from typing import List


class Solution:

    def binarySearch(self, i: int, m: int, matrix: List[List[int]], target: int):
        left = 0
        right = m - 1
        while left <= right:
            mid = floor((left + right) / 2)
            if matrix[i][mid] == target:
                return True
            if target < matrix[i][mid]:
                right = mid - 1

            else:
                left = mid + 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0] <= target and target <= matrix[i][m - 1]:
                return self.binarySearch(i, m, matrix, target)

        return False


print(Solution().searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))
print(Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15))
