from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum = 0
        mxscore = 0
        for i in range(k):
            sum += cardPoints[i]
        mxscore = sum
        left = k - 1
        right = len(cardPoints) - 1
        while left >= 0:
            sum -= cardPoints[left]
            sum += cardPoints[right]
            mxscore = max(sum, mxscore)
            right -= 1
            left -= 1

        return mxscore


print(Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3))
print(Solution().maxScore([2, 2, 2], 2))
print(Solution().maxScore([9, 7, 7, 9, 7, 7, 9], 7))
print(Solution().maxScore([11,49,100,20,86,29,72], 4))
