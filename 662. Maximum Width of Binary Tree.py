from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append((root, 1))
        max_width = 0
        while q:
            _, first_index = q[0]
            _, sec_index = q[-1]
            max_width = max(max_width, (sec_index - first_index) + 1)
            for _ in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, idx * 2))

                if node.right:
                    q.append((node.right, idx * 2 + 1))

        return max_width
