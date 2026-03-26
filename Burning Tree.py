from collections import deque


class Solution:
    def makeGraph(self, root, map):
        if not root:
            return

        if root.data not in map:
            map[root.data] = []

        if root.left:
            map[root.data].append(root.left.data)
            if root.left.data not in map:
                map[root.left.data] = []
            map[root.left.data].append(root.data)

        if root.right:
            map[root.data].append(root.right.data)
            if root.right.data not in map:
                map[root.right.data] = []
            map[root.right.data].append(root.data)

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

    def minTime(self, root, target):
        adjList = {}
        self.makeGraph(root, adjList)
        dist = self.findDistance(adjList, target.data)
        ans = 0
        for key in dist:
            ans = max(ans, dist[key])

        return ans
