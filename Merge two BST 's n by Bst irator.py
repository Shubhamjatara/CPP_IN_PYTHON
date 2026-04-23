class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.pushAll(root)

    def pushAll(self, root):
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        root = self.stack.pop()
        self.pushAll(root.right)
        return root.data

    def hasNext(self) -> bool:
        return len(self.stack) != 0

    def top(self):
        return self.stack[-1].data


class Solution:
    def merge(self, root1, root2):
        ans = []
        ibst1 = BSTIterator(root1)
        ibst2 = BSTIterator(root2)

        while ibst1.hasNext() and ibst2.hasNext():
            if ibst1.top() <= ibst2.top():
                ans.append(ibst1.top())
                ibst1.next()
            else:
                ans.append(ibst2.top())
                ibst2.next()

        while ibst1.hasNext():
            ans.append(ibst1.top())
            ibst1.next()

        while ibst2.hasNext():
            ans.append(ibst2.top())
            ibst2.next()

        return ans
