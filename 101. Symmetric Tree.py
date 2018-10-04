# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # tl: root of left tree; tr: root of right tree
        def judge(tl, tr):
            if not tl and not tr:
                return True
            elif not tl or not tr:
                return False
            return judge(tl.left, tr.right) and judge(tl.right, tr.left) if tl.val == tr.val else False

        return judge(root.left, root.right) if root else True
