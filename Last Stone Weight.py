import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []

        for t in stones:
            heapq.heappush(arr, -t)

        while len(arr) > 1:
            y = -heapq.heappop(arr)
            x = -heapq.heappop(arr)

            if x <= y:
                if x != y:
                    heapq.heappush(arr, -(y - x))

        if len(arr) == 1:
            return -arr[0]
        return 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(Solution().lastStoneWeight([1]))
print(Solution().lastStoneWeight([2, 2]))
