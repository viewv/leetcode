# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ptA, ptB, jumpToNext = headA, headB, False
        while ptA and ptB:
            if ptA == ptB:
                return ptA
            ptA, ptB = ptA.next, ptB.next
            if not ptA and not jumpToNext:
                ptA, jumpToNext = headB, True
            if not ptB:
                ptB = headA
        return None
