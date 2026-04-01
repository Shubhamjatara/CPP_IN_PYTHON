class Solution:
    def inorder(self, root, result, key):
        if root is None:
            return
        self.inorder(root.left, result, key)
        if root.data < key:
            result.append(root.data)
        self.inorder(root.right, result, key)

    def getInorder(self, root, key):
        result = []
        self.inorder(root, result, key)
        return result

    def findTarget(self, root, target):
        inorder = self.getInorder(root, target)
        left = 0
        right = len(inorder) - 1
        while left < right:
            sum = inorder[left] + inorder[right]
            if sum == target:
                return True

            if sum > target:
                right -= 1
            else: 
                left += 1
                
        return False
