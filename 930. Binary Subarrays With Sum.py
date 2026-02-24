from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        map = {}
        map[0] = 1
        curr = 0
        result = 0
        for num in nums:
            curr += num

            if curr - goal in map:
                result += map[curr - goal]

            if curr not in map:
                map[curr] = 1
            else:
                map[curr] += 1
        
        return result        


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))
print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0))
print(Solution().numSubarraysWithSum([0, 0, 0], 0))
