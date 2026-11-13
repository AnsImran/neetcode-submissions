class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] > self.heap[i//2]:
            tmp               = self.heap[i]
            self.heap[i]      = self.heap[i//2]
            self.heap[i // 2] = tmp
            i                 = i//2

    def pop(self):
        if len(self.heap) <= 1:
            return
        if len(self.heap) == 2:
            return self.heap.pop()
        result = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[2*i + 1] > self.heap[2*i] and self.heap[2*i + 1] > self.heap[i]:
                TMP = self.heap[i]
                self.heap[i] = self.heap[2*i + 1]
                self.heap[2*i + 1] = TMP
                i = 2*i + 1
            elif self.heap[2*i] > self.heap[i]:
                TMP = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = TMP
                i = 2*i
            else:
                break
        return result


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = MaxHeap()
        for s in stones:
            h.push(s)
        while len(h.heap) > 2:
            y = h.pop()
            x = h.pop()
            if y != x:
                h.push(y - x)
        if len(h.heap) == 2:
            return h.heap[1]
        return 0


########

# import heapq

# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         heap = []
#         for s in stones:
#             heap.append(-s)
#         heapq.heapify(heap)
#         while len(heap) >= 2:
#             y = -heapq.heappop(heap)
#             x = -heapq.heappop(heap)
#             if y != x:
#                 heapq.heappush(heap, -(y - x))
#         if heap:
#             return -heap[0]
#         return 0
