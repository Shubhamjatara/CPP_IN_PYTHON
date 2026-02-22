from math import floor
from typing import List


class Solution:
    def search(self, nums: List[int], left: int, right: int) -> int:

        mid = floor((left + right) / 2)
        minValue = 10 * 100
        while left <= right:
            mid = floor((left + right) / 2)
            if nums[mid] < nums[right]:
                minValue = min(minValue, nums[mid])
                right = mid - 1
            else:
                minValue = min(minValue, nums[left])
                left = mid + 1

        return minValue

    def findMin(self, nums: List[int]) -> int:

        return self.search(nums, 0, len(nums) - 1)


print(Solution().findMin([3, 4, 5, 6, 1, 2]))
print(Solution().findMin([4, 5, 0, 1, 2, 3]))
print(Solution().findMin([4, 5, 6, 7]))
print(Solution().findMin([5, 6, 7, 8, 9, 1, 2, 3, 4]))
