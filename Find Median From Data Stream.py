import heapq


class MedianFinder:

    def __init__(self):
        self.heap = []

    def print(self):
        print(self.heap)

    def addNum(self, num: int) -> None:

        heapq.heappush(self.heap, num)

    """ def findMedian(self) -> float:
        heapq.heapify(self.heap)
        lenth_of_healp = len(self.heap)
        mid = int(lenth_of_healp / 2)
        ans = 0
        if len(self.heap) % 2 == 0:
            ans = (self.heap[mid] + self.heap[mid - 1]) / 2
        else:
            ans = self.heap[mid]

        return ans """

    def findMedian(self) -> float:

        ans = 0
        temp = []
        while len(self.heap) != 0:
            temp.append(heapq.heappop(self.heap))

        lenth_of_healp = len(temp)
        mid = int(lenth_of_healp / 2)

        if len(temp) % 2 == 0:
            ans = (temp[mid] + temp[mid - 1]) / 2
        else:
            ans = temp[mid]

        for i in temp:
            heapq.heappush(self.heap, i)
        return float(ans)


a = MedianFinder()
arr = [
    [],
    [6],
    [],
    [10],
    [],
    [2],
    [],
    [6],
    [],
    [5],
    [],
    [0],
    [],
    [6],
    [],
    [3],
    [],
    [1],
    [],
    [0],
    [],
    [0],
    [],
]
j = 0
for i in arr:
    if j == 0:
        j += 1
        continue
    if len(i) == 0:
        print(a.findMedian())
    else:
        a.addNum(i[0])
