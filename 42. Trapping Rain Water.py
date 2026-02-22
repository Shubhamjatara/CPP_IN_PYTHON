from typing import List


class Solution:
    """def ple(self, arr: List[int]) -> List[int]:

        ans = [-1] * len(arr)
        mostMax = 0
        for i in range(len(arr)):

            mostMax = max(mostMax, arr[i])
            ans[i] = mostMax
        return ans

    def nle(self, arr: List[int]) -> List[int]:

        ans = [len(arr)] * len(arr)
        mostMax = 0
        for i in range(len(arr) - 1, -1, -1):

            mostMax = max(mostMax, arr[i])
            ans[i] = mostMax
        return ans
    """

    def trap(self, height: List[int]) -> int:
        cnt = 0
        leftMax = height[0]
        rightMax = height[-1]
        left = 0
        right = len(height) - 1
        while left <= right:
            if leftMax < rightMax:
                leftMax = max(leftMax, height[left])
                cnt += leftMax - height[left]
                left += 1

            else:
                rightMax = max(rightMax, height[right])
                cnt += rightMax - height[right]
                right -= 1

        return cnt


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
