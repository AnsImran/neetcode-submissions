class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k    = k
        self.nums = nums
        self.heap = [0]

        for i in self.nums:
            self.add(i)


    def add(self, val: int) -> int:
        self.push(val)
        # if len(self.heap) > k:
        if len(self.heap) > self.k + 1:                    # CHANGED: self.k, + 1 for the dummy at index 0
            # self.pop_heap()
            self.pop()                                     # CHANGED: the method is called pop
        return self.heap[1]

    def push(self, val):
        self.heap.append(val)
        # i = len(self.heap[i]) - 1
        i = len(self.heap) - 1                             # CHANGED: the length of the list
        # while self.heap[i] > self.heap[i//2]:
        while i > 1 and self.heap[i] < self.heap[i//2]:    # CHANGED: min-heap (<), and stop at the root
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
            if 2 * i + 1 < len(self.heap) and self.heap[2*i + 1] < self.heap[2*i] and self.heap[2*i + 1] < self.heap[i]:
                TMP = self.heap[i]
                self.heap[i] = self.heap[2*i + 1]
                self.heap[2*i + 1] = TMP
                i = 2*i + 1
            elif self.heap[2*i] < self.heap[i]:
                TMP = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = TMP
                i = 2*i
            else:
                break
        return result
