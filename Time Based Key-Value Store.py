from math import floor
from typing import List


class TimeMap:

    def binarySearch(self, n: int, arr: List[int], target: int):
        left = 0
        right = n - 1
        ans = -1
        mid = floor((left + right) / 2)
        while left <= right:
            (_, timestamp) = arr[mid]
            if timestamp <= target:
                ans = mid
            if timestamp == target:
                ans = mid
                break

            if target < timestamp:
                right = mid - 1
                mid = floor((left + right) / 2)
            else:
                left = mid + 1
                mid = floor((left + right) / 2)

        return ans

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(value, timestamp)]
        else:
            self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ""
        arr = self.map[key]
        mid = self.binarySearch(len(arr), arr, timestamp)
        if mid == -1:
            return ""
        (value, _) = arr[mid]
        return value


timeMap = TimeMap()
timeMap.set("check", "one", 5)
timeMap.set("check", "two", 10)
print(timeMap.get("check", 7))
print(timeMap.get("nonexistent", 7))
