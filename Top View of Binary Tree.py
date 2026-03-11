from collections import deque


class Solution:

    def topView(self, root):
        map = {}
        if not root:
            return []

        q = deque([(root, 0)])
        while q:
            node, hd = q.popleft()

            if hd not in map:
                map[hd] = node.data

            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        ans = []
        for key in sorted(map):
            ans.append(map[key])

        return ans
    
    
