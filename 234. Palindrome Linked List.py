# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list = []
        curr = head
        while curr != None:
            list.append(curr.val)
            curr = curr.next
        Flist = list[::-1]
        return list == Flist
