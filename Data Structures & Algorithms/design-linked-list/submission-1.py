class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val  = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.dummy_head = Node()
        self.dummy_tail = Node()

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

        self.size = 0


    def _get_node(self, index:int) -> int:
        if index < self.size//2:
            node = self.dummy_head.next
            for _ in range(index):
                # it'll work even if size=1 -> range=0 -> 
                # loop body never runs and NO ERROR as well.
                # Here you CAN do whatever you wanna do with the node
                # At the end increment it
                node = node.next
            return node
        else:
            node = self.dummy_tail.prev
            for _ in range(self.size-1-index):
                # Here you CAN do whatever you wanna do with the node
                # At the end increment it
                node = node.prev    
            return node   

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        else:
            return self._get_node(index).val

    def addAtHead(self, val: int) -> None:
        old_head  = self.dummy_head.next
        new_head  = Node(val, None, None)

        self.dummy_head.next = new_head  # new head is now real head
        new_head.next        = old_head  # prev head now after new head
        old_head.prev        = new_head  # prev of prev is now new head
        new_head.prev        = self.dummy_head
        
        self.size           += 1

    def addAtTail(self, val: int) -> None:
        prev_tail = self.dummy_tail.prev
        new_tail  = Node(val, None, None)

        self.dummy_tail.prev = new_tail
        new_tail.prev        = prev_tail
        prev_tail.next       = new_tail
        new_tail.next        = self.dummy_tail

        self.size           += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        else:
                next_node = self._get_node(index)
                node      = Node(val, None, None)
                prev_node = next_node.prev

                prev_node.next = node
                node.next      = next_node
                next_node.prev = node
                node.prev      = prev_node

                self.size     += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        else:
            node      = self._get_node(index)
            prev_node = node.prev
            next_node = node.next

            prev_node.next = next_node
            next_node.prev = prev_node

            node.next      = None
            node.prev      = None
            node.val       = None

            self.size     -= 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)