from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()

    def _reverse_stack(self):
        temp_q = deque()
        while self.empty() != True:
            temp_q.appendleft(self.stack.popleft())
        self.stack = temp_q

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        # reverse the que & peek at the front element, reverse back
        self._reverse_stack()
        top_element = self.stack.popleft()
        self._reverse_stack()
        return top_element

    def top(self) -> int:
        # reverse the que & peek at the front element, reverse back
        self._reverse_stack()
        if self.empty != True:
            top_element = self.stack[0]
        self._reverse_stack()
        return top_element

    def empty(self) -> bool:
        length = len(self.stack)
        if length == None or length == 0:
            return True
        else:
            return False
        
# use queue (deque)
# using len do EMPTY
# using append right do PUSH
# uisng peek/pop right to reverse the order do POP/TOP

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()