from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        curr = -1
        for i in range(len(asteroids)):

            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack and stack[-1] < abs(asteroids[i]):
                    stack.pop()
                if stack and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                    curr = i
                    break
                if stack and stack[-1] > abs(asteroids[i]):
                    curr = i
                    break

            if ((stack and stack[-1] < 0 and asteroids[i] < 0) or (
                stack and stack[-1] > 0 and asteroids[i] > 0
            )) and curr!=i:
                stack.append(asteroids[i])
                

            elif stack and stack[-1] < 0 and asteroids[i] > 0 and curr!=i:
                stack.append(asteroids[i])
                

            elif curr != i:
                stack.append(asteroids[i])

        return stack


print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([3, 5, -6, 2, -1, 4]))
print(Solution().asteroidCollision([-1, -2, 2, 1]))
print(Solution().asteroidCollision([-1, -1, 1, -1, 5]))
