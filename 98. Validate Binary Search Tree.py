from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def helper(self, root, min_r, max_r):
        if root is None:
            return True

        if  (root.val <= min_r or root.val >= max_r):
            return False

        return self.helper(root.left, min_r, root.val) and self.helper(
            root.right, root.val, max_r
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
