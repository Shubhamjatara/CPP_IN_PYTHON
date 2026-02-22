from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        heap = []
        arr = []
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1

        for x, y in map.items():
            heapq.heappush(heap, (-y, x))

        for i in range(k):
            [x, y] = heapq.heappop(heap)
            arr.append(y)

        return arr


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
print(Solution().topKFrequent([3,0,1,0], 1))