# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        if not root.left and not root.right:
            return [root.val, root.val]

        left = self.helper(root.left)
        right = self.helper(root.right)

        if root.left and not root.right:
            """maxSum = max(root.val, left[1], root.val + left[1])"""
            if root.val > left[1]:
                return [root.val,root.val]

        if not root.left and root.right:
            """maxSum = max(root.val, right[1], root.val + right[1])"""
            pathSum = right[1] + root.val if right[1] > root.val else root.val
            return [max(right[1], pathSum), pathSum]

        pathSum = max(left[1], right[1])

        if pathSum > root.val:
            return [max(pathSum, root.val, root.val + pathSum), pathSum + root.val]

        return [max(pathSum, root.val), root.val]

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[0]
