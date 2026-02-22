import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] = map[c] + 1

        for k, v in map.items():
            heapq.heappush(heap, (-v, k))

        temp_str = ""
        while heap:
            temp = []

            if heap:
                (v, k) = heapq.heappop(heap)
                if len(temp_str) == 0 or temp_str[len(temp_str) - 1] != k:
                    temp.append((v + 1, k))
                    temp_str = temp_str + k

            if heap:
                (v, k) = heapq.heappop(heap)
                if len(temp_str) == 0 or temp_str[len(temp_str) - 1] != k:
                    temp.append((v + 1, k))
                    temp_str = temp_str + k

            for v, k in temp:
                if v < 0:
                    heapq.heappush(heap, (v, k))

        if len(temp_str) != len(s):
            return ""
        return temp_str


print(Solution().reorganizeString("aab"))
""" print(Solution().reorganizeString("vvvlo")) """
