# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional
from queue import Queue


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = Queue()
        q.put([root])
        result = [[root.val]]
        flag = False
        while not q.empty():
            poped = q.get()

            temp = []
            temp_result = []
            for node in poped:
                if node and node.left:
                    temp.append(node.left)
                    temp_result.append(node.left.val)
                if node and node.right:
                    temp.append(node.right)
                    temp_result.append(node.right.val)

            if temp:
                q.put(temp)
                result.append(temp_result)

        for arr in result:
            if flag:
                arr.reverse()
            flag = not flag

        return result
