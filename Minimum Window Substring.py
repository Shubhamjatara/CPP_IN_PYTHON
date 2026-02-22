from typing import List


class Solution:
    def isValid(self, m1: List[int], m2: List[int]):
        for i in range(123):
            if m1[i] > m2[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        temp_t = t
        temp_s = s
        mapt = [0] * 123
        maps = [0] * 223
        flg = True
        length = 10**100
        for c in temp_t:
            mapt[ord(c)] += 1

        left = 0
        right = 0
        start = 0
        end = 0
        while right < len(temp_s):

            if mapt[ord(temp_s[right])] > 0:
                maps[ord(temp_s[right])] += 1

            if self.isValid(mapt, maps):
                flg = False
                while left <= right:
                    valid = self.isValid(mapt, maps)
                    if valid and (right - left + 1) < length:
                        length = right - left + 1
                        start = left
                        end = right

                    if not valid:
                        break

                    if maps[ord(temp_s[left])] > 0:
                        maps[ord(temp_s[left])] -= 1

                    left += 1

            right += 1

        if flg:
            return ""
        ans = temp_s[start : end + 1]
        return ans


# ZODYX
print(Solution().minWindow("OUZODYXAZV", "XYZ"))
print(Solution().minWindow("xyz", "xyz"))
print(Solution().minWindow("x", "xy"))
print(Solution().minWindow("ab", "A"))
