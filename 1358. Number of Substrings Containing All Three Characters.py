class Solution:
    def check(self, map):
        for i in range(len(map)):
            if map[i] < 1:
                return False
        return True

    def numberOfSubstrings(self, s: str) -> int:
        map = [0] * 3
        right = 0
        cnt = 0
        left = 0
        while right < len(s):
            map[ord(s[right]) - ord("a")] += 1
            while self.check(map):

                cnt += len(s) - right
                map[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1
        return cnt


print(Solution().numberOfSubstrings("abc"))
print(Solution().numberOfSubstrings("abcabc"))
