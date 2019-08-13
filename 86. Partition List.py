# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = []
        right = []
        node = head
        while node != None:
            if node.val < x:
                left.append(node.val)
            else:
                right.append(node.val)
            node = node.next
        left += right
        node = head
        for num in left:
            node.val = num
            node = node.next
        return head
