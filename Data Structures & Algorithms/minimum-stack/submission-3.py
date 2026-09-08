class MinStack:

    def __init__(self):
        self.stack   = []
        self.max_min = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.max_min.append(val)
            self.stack.append(val)
        elif len(self.stack) != 0:
            self.stack.append(val)
            if val > self.max_min[-1]:
                temporary_holder = self.max_min[-1]
                self.max_min[-1] = val
                self.max_min.append(temporary_holder)
            elif val <= self.max_min[-1]:
                self.max_min.append(val)
        
    def pop(self) -> None:
        if self.stack[-1] == self.max_min[-1]:
            self.max_min.pop()
            self.stack.pop()
        else:
            temp_holder = self.max_min[-1]
            self.max_min.pop()
            self.max_min[-1] = temp_holder
            self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.max_min[-1]
        





