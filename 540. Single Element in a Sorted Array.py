from math import floor
from math import inf
from typing import List


class Solution:
    def bs(self, left: int, right: int, nums: List[int]) -> int:
        if left > right:
            return -1

        mid = floor((left + right) / 2)
        leftBound = -1 if mid - 1 < 0 else nums[mid - 1]
        rightBound = (inf) if mid + 1 >= len(nums) else nums[mid + 1]

        if nums[mid] != leftBound and nums[mid] != rightBound:
            return mid

        leftPart = self.bs(left, mid - 1, nums)
        if leftPart != -1:
            return leftPart
        rightPart = self.bs(mid + 1, right, nums)
        if rightPart != -1:
            return rightPart

        return -1

    def singleNonDuplicate(self, nums: List[int]) -> int:
        ans = self.bs(0, len(nums) - 1, nums)
        if ans == -1:
            return -1
        return nums[ans]


print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
