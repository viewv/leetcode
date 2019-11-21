# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        queue = []
        nex = []
        queue.append(root)
        if not root:
            return []
        while queue:
            l = len(queue)
            temp = []
            nex = []
            for x in queue:
                temp.append(x.val)
                if x.left:
                    nex.append(x.left)
                if x.right:
                    nex.append(x.right)
            ans.append(temp)
            queue = nex
        return ans
