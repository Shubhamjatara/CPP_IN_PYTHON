from typing import List
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        heap = []
        map = {}
        for num in hand:

            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        for num, fre in map.items():
            heapq.heappush(heap, (num, fre))

        while heap:
            arr = []
            temp = []
            for _ in range(groupSize):
                if heap:
                    (num, fre) = heapq.heappop(heap)
                    arr.append(num)
                    temp.append((num, fre - 1))

            if len(arr) != groupSize:
                return False

            for i in range(len(arr) - 1):
                if abs(arr[i] - arr[i + 1]) != 1:
                    return False

            for num, fre in temp:
                if fre > 0:
                    heapq.heappush(heap, (num, fre))

        return True


print(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
print(Solution().isNStraightHand([1, 2, 3, 4, 5], 4))
