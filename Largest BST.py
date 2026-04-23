class Solution:

    def helper(self, root):

        if root is None:
            return [float("-inf"), float("inf"), 0]

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left[0] < root.data and root.data < right[1]:
            if left[0] == float("-inf") and right[1] == float("inf"):
                return [root.data, root.data, 1]

            if left[0] != float("-inf") and right[1] != float("inf"):
                size = left[2] + right[2] + 1
                return [min(left[0], root.data), max(root.data, right[1]), size]

            if left[0] == float("-inf"):
                size = right[2] + 1
                return [min(root.data, right[1]), max(root.data, right[1]), size]
            else:
                size = left[2] + 1
                return [min(root.data, left[0]), max(root.data, left[0]), size]

        return [float("inf"), float("-inf"), 0]

    def largestBst(self, root):
        ans = self.helper(root)
        return ans[2]
