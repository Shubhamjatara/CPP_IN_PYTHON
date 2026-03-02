from typing import List


class Solution:
    def mostAt(self, nums: List[int], k: int):
        left = 0
        right = 0
        map = {}
        count = 0
        while right < len(nums):

            if nums[right] in map:
                map[nums[right]] += 1
            else:
                map[nums[right]] = 1 

            while len(map) > k and left < right:
                map[nums[left]] -= 1
                if map[nums[left]] == 0:
                    del map[nums[left]]
                left += 1

            if len(map) <= k:
                count += right - left + 1

            right += 1

        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.mostAt(nums, k) - self.mostAt(nums, k - 1) 


print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
