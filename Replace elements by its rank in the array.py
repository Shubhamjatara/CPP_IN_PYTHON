import heapq


class Solution:
    def replaceWithRank(self, N, arr):
        map = {}
        heap = []
        for num in arr:
            if num not in map:
                map[num] = -1
                heapq.heappush(heap, num)

        rank = 0

        while heap:
            rank += 1
            poped = heapq.heappop(heap)
            map[poped] = rank

        ans = []

        for j in arr:
            ans.append(map[j])

        return ans


print(Solution().replaceWithRank(6, [20, 15, 26, 2, 98, 6]))
print(Solution().replaceWithRank(4, [2, 2, 1, 6]))
