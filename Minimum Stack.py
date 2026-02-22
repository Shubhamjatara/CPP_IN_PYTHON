class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
            return
        top = self.stack[len(self.stack) - 1]
        minVal = min(val, top[1])
        self.stack.append([val, minVal])

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.min = 10 * 100

    def top(self) -> int:
        top = self.stack[len(self.stack) - 1]
        return top[0]

    def getMin(self) -> int:
        top = self.stack[len(self.stack) - 1]
        return top[1]
