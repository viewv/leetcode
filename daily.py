from typing import List
import heapq


class BigHeap:
    arr = []

    def init(self):
        self.arr = list()

    def heap_insert(self, val):
        heapq.heappush(self.arr, -val)

    def heapify(self):
        heapq.heapify(self.arr)

    def heap_pop(self):
        return - heapq.heappop(self.arr)

    def heap_size(self):
        return len(self.arr)

    def get_top(self):
        if not self.arr:
            return
        return - self.arr[0]


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = BigHeap()
        for x in stones:
            h.heap_insert(x)
        while h.heap_size() > 1:
            y = h.heap_pop()
            x = h.heap_pop()
            if x != y:
                h.heap_insert(y - x)
        if h.heap_size() == 0:
            return 0
        return h.heap_pop()


sol = Solution()
print(sol.lastStoneWeight([1]))
