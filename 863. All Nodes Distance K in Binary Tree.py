from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def makeGraph(self, root: TreeNode, map):
        if not root:
            return

        if root.val not in map:
            map[root.val] = []

        if root.left:
            map[root.val].append(root.left.val)
            if root.left.val not in map:
                map[root.left.val] = []
            map[root.left.val].append(root.val)

        if root.right:
            map[root.val].append(root.right.val)
            if root.right.val not in map:
                map[root.right.val] = []
            map[root.right.val].append(root.val)

        self.makeGraph(root.left, map)
        self.makeGraph(root.right, map)

    def findDistance(self, adjList, target: int):
        visited = {}
        q = deque([(target, 0)])
        while q:
            (node, dis) = q.popleft()
            visited[node] = dis
            for neigbour in adjList[node]:
                if neigbour not in visited:
                    q.append((neigbour, dis + 1))

        return visited

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjList = {}
        self.makeGraph(root, adjList)
        dist  = self.findDistance(adjList,target.val)
        ans = []
        for key in dist:
            if dist[key] == k:
                ans.append(key)

        return ans
