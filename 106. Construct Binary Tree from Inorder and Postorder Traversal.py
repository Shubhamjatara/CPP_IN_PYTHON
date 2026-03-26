class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def build(self, postOrder, postIndex, inorder_map, start, end):

        if start > end:
            return None

        val = postOrder[postIndex[0]]
        root = TreeNode(val)
        postIndex[0] -= 1
        index = inorder_map[val]

        root.right = self.build(postOrder, postIndex, inorder_map, index + 1, end)
        root.left = self.build(postOrder, postIndex, inorder_map, start, index - 1)
        
        return root

    def buildTree(self, inorder: List[int], postOrder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        return self.build(postOrder, [len(postOrder)-1], inorder_map, 0, len(postOrder) - 1)
