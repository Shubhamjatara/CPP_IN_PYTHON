class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def __init__(self):
        self.first = None
        self.mid = None
        self.last = None
        self.pre = None

    def inorder(self, root):

        if root is None:
            return

        self.inorder(root.left)

        if self.pre and (self.pre.val > root.val):

            if self.first is None:
                self.first = self.pre
                self.mid = root
            else:
                self.last = root

        self.pre = root
        self.inorder(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:

        self.inorder(root)

        if self.first and self.last:
            a = self.first.val
            b = self.last.val
            self.last.val = a
            self.first.val = b

        elif self.first and self.mid:
            a = self.first.val
            b = self.mid.val
            self.first.val = b
            self.mid.val = a
