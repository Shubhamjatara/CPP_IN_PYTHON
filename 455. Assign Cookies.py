from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = len(g) - 1  # greed
        j = len(s) - 1  # cookies
        cnt = 0
        while 0 <= i and 0 <= j:
            if s[j] >= g[i]:
                cnt += 1
                i -= 1
                j -= 1
            else:
                i-=1

        return cnt        
    
    
print(Solution().findContentChildren([1,2,3],[1,1]))    
print(Solution().findContentChildren([1,2],[1,2,3]))  