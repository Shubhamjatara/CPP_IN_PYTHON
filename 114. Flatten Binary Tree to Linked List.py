from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root

        while curr:

            if curr.left is None:

                curr = curr.right
            else:

                leftChild = curr.left
                while leftChild.right and leftChild.right != curr:
                    leftChild = leftChild.right

                if leftChild.right is None:

                    leftChild.right = curr
                    curr = curr.left
                else:
                    curr_left = curr.left
                    curr_right = curr.right
                    curr.left = None
                    curr.right = curr_left
                    leftChild.right = curr_right

                    curr = curr.right
