class Solution:
    def pre(self, root, key, diff, ans):
        if root is None:
            return

        if (root.data < key) and ((key - root.data) < diff[0]):
            diff[0] = key - root.data
            ans[0] = root.data

        node = root.left if key <= root.data else root.right
        self.pre(node, key, diff, ans)

    def suc(self, root, key, diff, ans):
        if root is None:
            return

        if (root.data > key) and ((root.data - key) < diff[0]):
            diff[0] = root.data - key
            ans[1] = root.data

        node = root.right if key >= root.data else root.left
        self.suc(node, key, diff, ans)

    def findPreSuc(self, root, key):
        ans = [None, None]
        self.pre(root, key, [float("inf")], ans)
        self.suc(root, key, [float("inf")], ans)
        return ans
