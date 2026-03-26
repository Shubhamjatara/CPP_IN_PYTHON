from typing import List, Optional
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        encoded = []
        q = deque()
        q.append((root))
        encoded.append(root.val)
        while q:
            node = q.popleft()
            if node.left:
                encoded.append(node.left.val)
                q.append((node.left))
            else:
                encoded.append(None)

            if node.right:
                encoded.append(node.right.val)
                q.append((node.right))
            else:
                encoded.append(None)
        encoded_str = ",".join("#" if x is None else str(x) for x in encoded)
        print(isinstance(encoded_str, str))
        return encoded_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        decoded = [None if x == "#" else int(x) for x in data.split(",")]
        pnt = 0
        q = deque()
        root = TreeNode(decoded[pnt])
        q.append(root)

        while q:
            node = q.popleft()
            pnt += 1
            left = decoded[pnt]

            if left:
                leftNode = TreeNode(left)
                node.left = leftNode
                q.append(leftNode)
            else:
                node.left = left

            pnt += 1
            right = decoded[pnt]
            if right:
                rightNode = TreeNode(right)
                node.right = rightNode
                q.append(rightNode)
            else:
                node.right = right

        return root
