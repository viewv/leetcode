# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        maxdepth = 1
        head = root

        def dfs(head):
            nonlocal maxdepth
            if not head:
                return 0
            l = dfs(head.left)
            r = dfs(head.right)
            maxdepth = max(maxdepth, l+r+1)
            return max(l, r) + 1
        dfs(head)
        return maxdepth - 1


root = TreeNode(1)
a = TreeNode(2)
a1 = TreeNode(4)
a2 = TreeNode(5)
a.left = a1
a.right = a2
b = TreeNode(3)
root.left = a
root.right = b
sol = Solution()
print(sol.diameterOfBinaryTree(root))
