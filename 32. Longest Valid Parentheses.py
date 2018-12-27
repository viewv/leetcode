class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        stack = []
        s = list(s)
        for x in s:
            if x == '(':
                stack.append(x)
            if x == ')':
                if len(stack) != 0:
                    ans += 2
                    stack.pop()
        return ans
