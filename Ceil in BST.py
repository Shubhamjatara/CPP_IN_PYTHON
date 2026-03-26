class Solution:
    def search(self, root, x, ans):
        if root is None:
            return False
        if root.data == x:
            ans[0] = x
            return True
        if root.data > x:
            ans[0] = root.data

        node = root.left if x < root.data else root.right
        if self.search(node, x, ans):
            return True

        return False

    def findCeil(self, root, x):
        ans = [-1]
        self.search(root, x, ans)
        return ans[0]
