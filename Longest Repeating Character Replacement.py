class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0] * 26
        left = 0
        right = 0
        ans = 0
        while left <= right and right < len(s):

            arr[ord(s[right]) - 65] += 1
            largest = max(arr)
            diff = abs(((right - left) + 1) - largest)
            if diff <= k:
                ans = max(ans, ((right - left) + 1))

            if diff > k:
                arr[ord(s[left]) - 65] -= 1
                arr[ord(s[right]) - 65] -= 1
                left += 1
                continue

            right += 1

        return ans


print(Solution().characterReplacement("XYYX", 2))
print(Solution().characterReplacement("AAABABB", 1))
print(Solution().characterReplacement("AABABBA", 1))
