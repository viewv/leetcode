class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Sentinel node at both front and back of the list
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self._inRange(index, 0, self.size-1):
            return self._getNodeAt(index).val
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if self._inRange(index, 0, self.size):
            curr = self._getNodeAt(index)
            new = ListNode(val)
            new.next = curr
            new.prev = curr.prev
            curr.prev.next = new
            curr.prev = new
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if self._inRange(index, 0, self.size-1):
            curr = self._getNodeAt(index)
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.size -= 1

    def _inRange(self, index, start, end):
        return start <= index <= end

    def _getNodeAt(self, index):
        if index < self.size // 2:
            curr = self.head
            for _ in range(-1, index):
                curr = curr.next
        else:
            # go backwards
            curr = self.tail
            for _ in range(self.size, index, -1):
                curr = curr.prev
        return curr
