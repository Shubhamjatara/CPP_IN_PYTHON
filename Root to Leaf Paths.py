class Solution:
    def helper(self, root, ans, path):
        if not root:
            return

        path.append(root.data)

        if not root.left and not root.right:
            ans.append(path.copy())
            path.pop()
            return

        self.helper(root.left, ans, path)
        self.helper(root.right, ans, path)
        path.pop()

    def Paths(self, root):
        ans = []
        self.helper(root, ans, [])
        return ans
