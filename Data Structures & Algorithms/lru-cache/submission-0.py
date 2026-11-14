class Node:
    def __init__(self, val=None, prev=None, nex=None):
        self.val  = val
        self.prev = prev
        self.nex  = nex

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru      = {}
        self.usage    = {}

        self.head = Node()
        self.tail = Node()

        self.tail.prev = self.head
        self.head.nex  = self.tail

    def get(self, key: int) -> int:
        if key in self.lru:
            self.update_usage(key)
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.lru[key] = value

        self.update_usage(key)

        if len(self.lru) > self.capacity:
            self.remove_lru_key()

    
    def add_to_head(self, current_node):
        # get the node that will be next to the current node
        nex = self.head.nex

        # updating forward pointing arrows
        # place current node at head
        self.head.nex    = current_node
        # place the node that was to be next to current node, next to current_node
        current_node.nex = nex

        # updating backward pointing arrows
        # update the prev connection of old at head node
        nex.prev          = current_node
        # update the prev connection of current node towards head
        current_node.prev = self.head 
    
    def update_usage(self, key):
        if key not in self.usage:
            # create current node 
            current_node    = Node(key, None, None)

            # add curent node to `usage` hash map
            self.usage[key] = current_node

            # place the current node at head
            self.add_to_head(current_node)
        else:
            # get current node
            current_node = self.usage[key]

            # get prev and next of current node
            nex  = current_node.nex
            prev = current_node.prev
            
            # connect prev and next AND isolate current
            prev.nex = nex
            nex.prev = prev
            
            # add current to head
            self.add_to_head(current_node)

    def remove_lru_key(self):
        to_remove = self.tail.prev
        prev      = to_remove.prev

        self.tail.prev = prev
        prev.nex       = self.tail

        self.lru.pop(to_remove.val)
        self.usage.pop(to_remove.val)
    
















        
