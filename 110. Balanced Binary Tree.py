# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        elif abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if root == None:
            return 0
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        return (leftDepth if leftDepth > rightDepth else rightDepth)+1
