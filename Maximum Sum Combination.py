import heapq


class Solution:
    def topKSumPairs(self, a, b, k):
        n = len(a)
        a.sort(reverse=True)
        b.sort(reverse=True)
        heap = []
        visited = set()
        heapq.heappush(heap, (-(a[0] + b[0]), (0, 0)))
        visited.add((0, 0))
        ans = []
        while heap and k:
            sum, (i, j) = heapq.heappop(heap)

            ans.append(-sum)
            if i + 0 < n and j + 1 < n and (i + 0, j + 1) not in visited:
                heapq.heappush(heap, (-(a[i + 0] + b[j + 1]), (i + 0, j + 1)))
                visited.add((i + 0, j + 1))

            if i + 1 < n and j + 0 < n and (i + 1, j + 0) not in visited:
                heapq.heappush(heap, (-(a[i + 1] + b[j + 0]), (i + 1, j + 0)))
                visited.add((i + 1, j + 0))

            k -= 1

        return ans


print(Solution().topKSumPairs([3, 2], [1, 4], 2))
print(Solution().topKSumPairs([1, 4, 2, 3], [2, 5, 1, 6], 3))
