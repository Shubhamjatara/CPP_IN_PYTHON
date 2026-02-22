from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append(
                [position[i], speed[i], float((target - position[i]) / speed[i])]
            )
        arr.sort(key=lambda x: x[0])
        stack = []
        for i in range(len(arr)):

            while stack and arr[i][2] >= stack[len(stack) - 1][2]:
                stack.pop()

            stack.append(arr[i])

        return len(stack)


print(Solution().carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]))
print(Solution().carFleet(10, [1, 4], [3, 2]))
print(Solution().carFleet(10, [3], [3]))
print(Solution().carFleet(100, [0, 2, 4], [4, 2, 1]))
print(Solution().carFleet(10, [8,3,7,4,6,5], [4,4,4,4,4,4]))
