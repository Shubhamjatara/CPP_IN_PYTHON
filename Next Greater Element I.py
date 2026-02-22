from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * (max(nums2) + 1)
        stack = []
        final_ans = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()

            if stack:
                ans[nums2[i]] = stack[-1]

            stack.append(nums2[i])
        for j in range(len(nums1)):
            final_ans.append(ans[nums1[j]])
        return final_ans


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
