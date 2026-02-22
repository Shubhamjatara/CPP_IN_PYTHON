from typing import List


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[len(stack) - 1]]:
                stack.pop()

            if not stack:
                ans[i] = 0

            else:
                ans[i] = stack[len(stack) - 1] - i

            stack.append(i)

        return ans


print(Solution().dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))
print(Solution().dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
