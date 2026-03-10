class Solution:
    def traverseLeft(self, root, arr):
        if not root:
            return False

        if not root.left and not root.right:
            return True

        arr.append(root.data)
        if self.traverseLeft(root.left, arr):
            return True
        if self.traverseLeft(root.right, arr):
            return True

    def findLeaves(self, root, arr):

        if not root:
            return
        if not root.left and not root.right:
            arr.append(root.data)
            return

        self.findLeaves(root.left, arr)
        self.findLeaves(root.right, arr)

    def traverseRight(self, root, arr):
        if not root:
            return False

        if not root.left and not root.right:
            return True

        if self.traverseRight(root.right, arr):
            arr.append(root.data)
            return True
        if self.traverseRight(root.left, arr):
            arr.append(root.data)
            return True

    def boundaryTraversal(self, root):
        arr = []
        arr.append(root.data)
        self.traverseLeft(root.left, arr)
        self.findLeaves(root.left, arr)
        self.findLeaves(root.right, arr)
        self.traverseRight(root.right, arr)
        return arr
