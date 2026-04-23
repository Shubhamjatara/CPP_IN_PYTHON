from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root)

    def pushAll(self, root: Optional[TreeNode]):
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        root = self.stack.pop()
        self.pushAll(root.right)
        return root.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0
