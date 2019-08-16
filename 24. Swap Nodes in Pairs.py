class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy_node = ListNode(-1)
        dummy_node.next = head
        head = dummy_node

        prev, p1, p2 = head, head.next, head.next.next
        while True:
            tmp = p2.next
            p2.next = p1
            p1.next = tmp
            prev.next = p2

            if not p1.next or not p1.next.next:
                break

            prev = p1
            p1 = p1.next
            p2 = p1.next

        return head.next
