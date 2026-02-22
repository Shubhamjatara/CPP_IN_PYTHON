from typing import List
import heapq


class Solution:
    def Euclidean(self, x, y):
        return pow(0 - x, 2) + pow(0 - y, 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        close_point = []
        for p in points:
            ans = self.Euclidean(p[0], p[1])
            heap.append((ans, [p[0], p[1]]))

        heapq.heapify(heap)
        for i in range(k):
            poped = heapq.heappop(heap)
            close_point.append(poped[1])

        return close_point


print(Solution().kClosest([[1, 3], [-2, 2]], 1))
