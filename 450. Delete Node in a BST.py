from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertLeftMost(self, root, insertNode):
        if root.left is None:
            root.left = insertNode
            return
        self.insertLeftMost(root.left, insertNode)

    def delete(self, node):

        left = node.left
        right = node.right

        if right is None:
            return left

        self.insertLeftMost(right, left)
        return right

    def search(self, root, key):

        if root is None:
            return

        if root.left and root.left.val == key:
            root.left = self.delete(root.left)
            return

        if root.right and root.right.val == key:
            root.right = self.delete(root.right)
            return

        node = root.left if key < root.val else root.right
        self.search(node, key)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        if root.val == key:
            return self.delete(root)
        
        self.search(root, key)

        return root
