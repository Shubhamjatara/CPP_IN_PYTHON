from typing import List


class FreqStack:

    def __init__(self):
        self.stack = []
        self.stackMap = {}
        self.freqMap = {}

    def print(self):
        print(self.stack)
        print(self.stackMap)

    def push(self, val: int) -> None:
        if val in self.freqMap:
            self.freqMap[val] += 1
        else:
            self.freqMap[val] = 1

        freqOfVal = self.freqMap[val]

        if freqOfVal in self.stackMap:
            self.stackMap[freqOfVal].append(val)
        else:
            self.stackMap[freqOfVal] = [val]

        max_len = freqOfVal

        if self.stack and self.stack[-1] < max_len:
            self.stack.append(max_len)
            return

        if not self.stack:
            self.stack.append(max_len)

    def pop(self) -> int:
        top = self.stack[-1]
        poped = self.stackMap[top].pop()
        self.freqMap[poped] -= 1
        if len(self.stackMap[top]) == 0:
            self.stack.pop()
            del self.stackMap[top]

        return poped


obj = FreqStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(2)
print(obj.pop())
print(obj.pop())
print(obj.pop())


