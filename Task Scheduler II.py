from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        mp = {}
        time = 0

        for t in tasks:
            if t in mp:
                time = max(time, space + 1 + mp[t])

            mp[t] = time
            time += 1
        return time


x = Solution().taskSchedulerII([1, 2, 1, 2, 3, 1], 3)
print(x)
print(Solution().taskSchedulerII([5, 8, 8, 5], 2))
print(
    Solution().taskSchedulerII(
        [
            425,
            755,
            189,
            702,
            882,
            882,
            120,
            635,
            120,
            755,
            702,
            702,
            425,
            351,
            425,
            351,
            742,
            755,
            882,
            742,
            120,
            189,
            702,
            635,
            120,
            635,
            351,
            425,
            425,
            882,
            425,
            425,
            189,
            635,
            635,
            425,
            755,
            425,
            351,
            882,
            635,
            742,
            882,
            425,
            742,
            120,
            120,
            120,
            755,
            755,
            120,
            351,
            425,
            702,
            351,
            702,
            425,
            425,
            425,
        ],
        41,
    )
)
