class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cnt = 0
        while self.stack and price >= self.stack[-1][0]:
            cnt += self.stack[-1][1]
            self.stack.pop()

        self.stack.append([price, cnt + 1])
        return self.stack[-1][1]


sp = StockSpanner()
print(sp.next(100))
print(sp.next(80))
print(sp.next(60))
print(sp.next(70))
print(sp.next(60))
print(sp.next(75))
print(sp.next(85))
