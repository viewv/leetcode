# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        level = 0
        q.append((root, level))
        res = []
        pre = -1
        tmp = []

        if root is None:
            return []

        while (q):
            x, level = q.pop(0)

            if level == pre:
                tmp.append(x.val)
            else:
                if len(tmp) > 0:
                    res.append(tmp)
                    tmp = []
                tmp.append(x.val)

            pre = level
            level = level+1

            if x.left:
                q.append((x.left, level))
            if x.right:
                q.append((x.right, level))

        if len(tmp) > 0:
            res.append(tmp)

        return res[::-1]
