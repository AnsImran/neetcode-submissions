class MinStack:
    def __init__(self):
        self.stack = []              # each item: (val, min_so_far)

    def push(self, val):
        cur = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]