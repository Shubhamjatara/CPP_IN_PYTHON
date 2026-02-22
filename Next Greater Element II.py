from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i in range(2 * len(nums) - 1, -1, -1):
            while stack and stack[-1] <= nums[i % len(nums)]:
                stack.pop()

            if stack:
                ans[i % len(nums)] = stack[-1]

            stack.append(nums[i % len(nums)])

        return ans


print(Solution().nextGreaterElements([1, 2, 1]))
