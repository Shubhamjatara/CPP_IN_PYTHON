class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def insert(self, root: Optional[TreeNode], val: int):

        if val < root.val and root.left is None:
            root.left = TreeNode(val)
            return True

        if val > root.val and root.right is None:
            root.right = TreeNode(val)
            return True

        node = root.left if val < root.val else root.right
        if self.insert(node, val):
            return True

        return False

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        self.insert(root, val)

        return root

