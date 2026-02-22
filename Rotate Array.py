from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        left = 0
        right = k - 1
        nums.reverse()
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        left = k
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    


Solution().rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
Solution().rotate([1000, 2, 4, -3], 2)
Solution().rotate([1000, 2, 4, -3], 3)
