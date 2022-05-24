# https://leetcode.cn/problems/univalued-binary-tree/


from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_1:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        return self.check_val(root, val)

    def check_val(self, root, val):
        if root is None:
            return True

        if root.val != val:
            return False
        return self.check_val(root.left, val) and self.check_val(root.right, val)


class Solution_2:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = right = True

        if root.left:
            left = root.val == root.left.val and self.isUnivalTree(root.left)

        if root.right:
            right = root.val == root.right.val and self.isUnivalTree(root.right)

        return left and right


class Solution_3:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        q = Queue()
        q.put(root)
        while not q.empty():
            node = q.get()
            print(node.val)
            if node.val != val:
                return False
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return True
