class Solution:
    def minWindow(self, s1, s2):
        if len(s1) < len(s2):
            return ""

        n = len(s1)
        m = len(s2)

        min_len = float("inf")
        ans = ""

        i = 0
        while i < n:

            pnt = 0
            cnt = 0
            start = -1

            # ---------- Forward scan ----------
            while i < n:
                if s1[i] == s2[pnt]:
                    if cnt == 0:
                        start = i
                    cnt += 1
                    pnt += 1
                    if cnt == m:
                        break
                i += 1

            if i == n:
                break

            end = i

            # ---------- Backward scan ----------
            pnt = m - 1
            temp = end

            while temp >= start:
                if s1[temp] == s2[pnt]:
                    pnt -= 1
                    if pnt < 0:
                        start = temp
                        break
                temp -= 1

            # update answer
            if end - start + 1 < min_len:
                min_len = end - start + 1
                ans = s1[start : end + 1]

            # restart search
            i = start + 1

        return ans


print(Solution().minWindow("geeksforgeeks", "eksrg"))
print(Solution().minWindow("abcdebdde", "bde"))
print(Solution().minWindow("ad", "b"))
print(Solution().minWindow("defdfegdegeegdddeg", "deeg"))
