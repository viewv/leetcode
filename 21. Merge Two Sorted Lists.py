class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None or (l2 and l1.val>l2.val):
            l1, l2 = l2, l1
        tail = l1
        while tail and l2:
            if tail.next is None or (tail.next.val > l2.val):
                tail.next, l2 = l2, tail.next
            tail = tail.next
        return l1