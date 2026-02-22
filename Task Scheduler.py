import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        map = {}

        for c in tasks:
            if c not in map:
                map[c] = 1
            else:
                map[c] = map[c] + 1

        for _, v in map.items():
            heapq.heappush(heap, -v)

        time = 0

        while heap:
            temp = []

            for i in range(n + 1):
                if heap:
                    v = heapq.heappop(heap)
                    temp.append(v + 1)

            for t in temp:
                if t < 0:
                    heapq.heappush(heap, t)

            if len(heap)==0:
                time += len(temp)
            else:
                time += n + 1

        return time


""" 8 10 6 """
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 3))
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 1))
