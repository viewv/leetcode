# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        else:
            slow = head
            fast = head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
