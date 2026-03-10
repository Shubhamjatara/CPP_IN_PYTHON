import heapq


class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:

        temp = []
        while self.heap:
            temp.append(heapq.heappop(self.heap))
        n = len(temp)
        """ print(temp) """
        ans = 0.0
        mid = (0 + n - 1) // 2
        if n % 2 == 0:

            ans = ((temp[mid] + temp[mid - 1])) / 2
        else:
            ans = float(temp[mid])

        for t in temp:
            heapq.heappush(self.heap, t)

        return ans


mf = MedianFinder()
a = [-1, -2, -3, -4,-5]
for i in a:
    mf.addNum(i)
    print(mf.findMedian())
