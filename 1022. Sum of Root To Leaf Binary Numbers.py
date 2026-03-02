from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, root: Optional[TreeNode], b: str, path: List[str]):
        if not root:

            return

        if not root.left and not root.right:
            path.append((str(root.val) + b)[::-1])
            return

        self.traverse(root.left, str(root.val) + b, path)
        self.traverse(root.right, str(root.val) + b, path)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        path = []

        self.traverse(root, "", path)
        ans = 0
        for i in path:
            ans+=int(i,2)
        return ans
