# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional
from collections import deque


class Solution:

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        ans = []
        q = deque([(root, 0, 0)])

        while q:
            node, i, j = q.popleft()
            nodes.append((j, i, node.val))
            if node.left:
                q.append((node.left, i + 1, j - 1))

            if node.right:
                q.append((node.right, i + 1, j + 1))

        nodes.sort()
        prev = float("-inf")
        for c, r, val in nodes:
            if c != prev:
                ans.append([])
                prev = c
            ans[-1].append(val)
        return ans


Solution().verticalTraversal()
