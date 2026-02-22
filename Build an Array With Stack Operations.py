from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        t = 0
        st = []
        ans = []
        for i in range(1, n + 1, 1):
            if t >= len(target):
                continue

            if target[t] == i:
                while st and t - 1 >= 0 and target[t - 1] != st[-1]:
                    st.pop()
                    ans.append("Pop")

                while st and t == 0:
                    st.pop()
                    ans.append("Pop")

                t += 1

            st.append(i)
            ans.append("Push")

        return ans


print(Solution().buildArray([1, 3], 3))
print(Solution().buildArray([1, 2, 3], 3))
print(Solution().buildArray([1, 2], 4))
print(Solution().buildArray([2,3,4], 4))
