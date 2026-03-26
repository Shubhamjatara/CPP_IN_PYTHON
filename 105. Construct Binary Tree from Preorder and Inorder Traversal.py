class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def build(self, preOrder, preIndex, inorder_map, start, end):

        if start > end:
            return None

        val = preOrder[preIndex[0]]
        root = TreeNode(val)
        preIndex[0] += 1
        index = inorder_map[val]

        root.left = self.build(preOrder, preIndex, inorder_map, start, index - 1)
        root.right = self.build(preOrder, preIndex, inorder_map, index + 1, end)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        return self.build(preorder, [0], inorder_map, 0, len(preorder) - 1)
