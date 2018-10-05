# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack = []
        p = head
        while p != None:
            stack.append(p)
            p = p.next
        if len(stack) == 1:
            return None
        if len(stack) == n:
            head = stack[1]
            return head
        if n == 1:
            stack[-2].next = None
        else:
            stack[-1 * n - 1].next = stack[-1 * n + 1]
        return head
