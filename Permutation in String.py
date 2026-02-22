from typing import List


class Solution:

    def isValid(self, map1: List[int], map2: List[int]):

        for i in range(123):
            if map1[i] != map2[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        map1 = [0] * 123
        map2 = [0] * 123

        for c in s1:
            map1[ord(c)] += 1

        for i in range(len(s1)):
            map2[ord(s2[i])] += 1

        if self.isValid(map1, map2):
            return True

        left = 0
        right = len(s1)

        while left < right and right < len(s2):
            map2[ord(s2[right])] += 1

            if len(s1) < ((right - left) + 1):
                map2[ord(s2[left])] -= 1
                left += 1

            if self.isValid(map1, map2):
                return True

            right += 1

        return False


print(Solution().checkInclusion("abc", "lecabee"))
print(Solution().checkInclusion("abc", "lecaabee"))
print(Solution().checkInclusion("adc", "dcda"))
print(Solution().checkInclusion("abc", "cccccbabbbaaaa"))
