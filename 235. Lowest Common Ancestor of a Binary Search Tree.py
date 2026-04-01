from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root: "TreeNode", p: int, q: int, ansNode):

        if p < root.val and q < root.val:
            self.helper(root.left, p, q, ansNode)

        if p > root.val and q > root.val:
            self.helper(root.right, p, q, ansNode)

        if (p < root.val and q > root.val) or (p > root.val and q < root.val):
            ansNode[0] = root
            return

        if p == root.val:
            ansNode[0] = root
            return
        if q == root.val:
            ansNode[0] = root
            return

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        ans = None
        while root:

            if p.val < root.val and q.val < root.val:
                root = root.left

            if p.val > root.val and q.val > root.val:
                root = root.right

            if (p.val < root.val and q.val > root.val) or (
                p.val > root.val and q.val < root.val
            ):
                ans = root
                break

            if p.val == root.val:
                ans = root

                break
            if q.val == root.val:
                ans = root

                break
        return ans
