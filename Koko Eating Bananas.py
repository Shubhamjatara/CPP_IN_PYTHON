from math import ceil, floor
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = 1000000000
        while left <= right:
            mid = floor((left + right) / 2)
            k = mid
            temp = 0
            for i in piles:
                temp += ceil((i / k))

            if temp <= h:
                ans = min(ans, k)

            if temp <= h:
                right = mid - 1
            else:
                left = mid + 1

        return ans


print(Solution().minEatingSpeed([1, 4, 3, 2], 9))
print(Solution().minEatingSpeed([25, 10, 23, 4], 4))
print(Solution().minEatingSpeed([312884470], 312884469))
