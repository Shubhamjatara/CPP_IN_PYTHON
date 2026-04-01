from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bst(self, root, preorder: List[int], pre_ind: List[int], min_r, max_r):

        root = TreeNode(preorder[pre_ind[0]])
        
        if len(preorder) - 1 > pre_ind[0]:
            pre_ind[0] += 1
        if min_r < preorder[pre_ind[0]] < root.val:
            root.left = self.bst(root.left, preorder, pre_ind, min_r, root.val)

        if root.val < preorder[pre_ind[0]] < max_r:
            root.right = self.bst(root.right, preorder, pre_ind, root.val, max_r)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.bst(None, preorder, [0], float("-inf"), float("inf"))
