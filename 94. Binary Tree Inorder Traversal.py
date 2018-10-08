# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 中序遍历二叉树


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        p = root
        while p != None or len(stack) != 0:
            while p != None:
                stack.append(p)
                p = p.left
            if len(stack) != 0:
                p = stack.pop()
                ans.append(p.val)
                p = p.right
        return ans
