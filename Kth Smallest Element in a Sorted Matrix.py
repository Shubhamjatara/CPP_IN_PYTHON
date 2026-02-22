from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        col = len(matrix[0])
        row = len(matrix)
        visted = set()
        heap = []
        heapq.heappush(heap, (matrix[0][0], (0, 0)))
        visted.add((0, 0))
        ans = matrix[0][0]
        while heap and k > 0:

            val, (i, j) = heapq.heappop(heap)
            ans = val
            if i + 1 < row and (i + 1, j) not in visted:
                heapq.heappush(heap, (matrix[i + 1][j], (i + 1, j)))
                visted.add((i + 1, j))

            if j + 1 < col and (i, j + 1) not in visted:
                heapq.heappush(heap, (matrix[i][j + 1], (i, j + 1)))
                visted.add((i, j + 1))

            k = k - 1

        
        return ans


Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
Solution().kthSmallest([[-5]], 1)
Solution().kthSmallest([[1,2],[1,3]], 2)

