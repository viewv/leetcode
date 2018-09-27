# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        all = []
        for x in lists:
            temp = x
            while temp != None:
                all.append(temp.val)
                temp = temp.next
        return sorted(all)
