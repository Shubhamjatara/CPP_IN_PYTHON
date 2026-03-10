import heapq


class Solution:
    def minCost(self, arr):
        heap = []
        for rope in arr:
            heapq.heappush(heap, rope)

        total = 0
        while len(heap) > 1:
            rope1 = heapq.heappop(heap)
            rope2 = heapq.heappop(heap)
            total += rope1 + rope2
            heapq.heappush(heap, rope1 + rope2)

        return total


print(Solution().minCost([4, 3, 2, 6]))
print(Solution().minCost([4, 2, 7, 6, 9]))
print(Solution().minCost([10]))