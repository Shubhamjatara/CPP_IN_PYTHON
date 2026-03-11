from ast import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode", ans: List["TreeNode"]
    ) -> bool:
        if not root:
            return False

        left = self.helper(root.left, p, q, ans)
        right = self.helper(root.right, p, q, ans)

        if left and right:
            ans.append(root)
            return False

        if (left or right) and (root.val == p.val or root.val == q.val):
            ans.append(root)
            return False

        if left or right:
            return True

        if q.val == root.val or p.val == root.val:
            return True

        return False

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        ans = []
        self.helper(root, p, q, ans)
        return ans[0]
