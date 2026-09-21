class Node:
    def __init__(self, val="", prev=None, next=None):
        self.val  = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.dummy_head   = Node("", None, None)
        self.dummy_tail   = Node("", None, None)
        self.homepage     = Node(homepage, None, None)

        self.dummy_head.next = self.homepage
        self.homepage.next   = self.dummy_tail
        self.dummy_tail.prev = self.homepage
        self.homepage.prev   = self.dummy_head

        self.current_node  = self.homepage
        self.size          = 1
        self.current_index = 1

    def _get_index(self, direction:str, steps:int) -> int:
        if direction == "forward":
            index = self.current_index + steps
            if index > self.size:
                return self.size
            else:
                return index
        elif direction == "backward":
            index = self.current_index - steps
            if index < 1:
                return 1
            else:
                return index

    def _get_node(self, index: int):
        # can make it efficient by d/f b/w forward and backward dorections
        node = self.dummy_head
        for _ in range(index):
            node = node.next
        return node

    def visit(self, url: str) -> None:
        node      = Node(url, None, None)
        prev_node = self.current_node

        node.prev      = prev_node
        prev_node.next = node

        self.current_node   = node
        self.current_index += 1
        self.size           = self.current_index
        # update size

    def back(self, steps: int) -> str:
        # update index
        index = self._get_index('backward', steps)
        node  = self._get_node(index)

        self.current_node  = node 
        self.current_index = index
        return node.val

    def forward(self, steps: int) -> str:
        index = self._get_index(direction='forward', steps=steps)
        node  = self._get_node(index)

        self.current_node  = node 
        self.current_index = index
        return node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)