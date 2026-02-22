from math import floor
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = floor((left + right) / 2)
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[right]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1

        return -1


print(Solution().search([3,4,5,6,1,2],1))
print(Solution().search([3,5,6,0,1,2],4))