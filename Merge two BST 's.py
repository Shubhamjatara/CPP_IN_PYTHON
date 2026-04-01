class Solution:
    def inorder(self, root, result):
        if root is None:
            return
        self.inorder(root.left, result)
        result.append(root.data)
        self.inorder(root.right, result)

    def getInorder(self, root):
        result = []
        self.inorder(root, result)
        return result

    def merge(self, root1, root2):
        inorder_1 = self.getInorder(root1)
        inorder_2 = self.getInorder(root2)

        left = 0
        right = 0
        ans = []
        while left < len(inorder_1) and right < len(inorder_2):
            if inorder_1[left] <= inorder_2[right]:
                ans.append(inorder_1[left])
                left += 1
            else:
                ans.append(inorder_2[right])
                right += 1

        while left < len(inorder_1):
            ans.append(inorder_1[left])
            left += 1

        while right < len(inorder_2):
            ans.append(inorder_2[right])
            right += 1

        return ans
