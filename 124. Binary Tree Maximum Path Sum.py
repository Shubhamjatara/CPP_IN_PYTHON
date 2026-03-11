from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root: Optional[TreeNode], ans):
        if not root:
            return float("-inf")

        left = self.helper(root.left, ans)
        right = self.helper(root.right, ans)
        # find max path
        ans[0] = max(
            ans[0],
            root.val,
            # left,
            # right,
            root.val + left,
            root.val + right,
            root.val + left + right,
        )
        # choosing max path from left or right
        return max(left + root.val, right + root.val, root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float("-inf")]
        self.helper(root, ans)
        return ans[0]
