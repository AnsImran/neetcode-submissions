from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        visits = set()
        q      = deque()

        q.append(node)
        visits.add(node)

        new_node_1 = Node(node.val, [])
        if len(node.neighbors) == 0:
            return new_node_1

        length=0
        adjList = {}

        while q:
            for i in range(len(q)):
                current_node                  = q.popleft()
                new_current_node              = Node(current_node.val, []) ##
                if length==0:                                              ##
                    new_current_node = new_node_1                          ##
                adjList[new_current_node.val] = new_current_node           ##


                
                for neighbor in current_node.neighbors:
                    adjList[new_current_node.val].neighbors.append(neighbor.val) ##
                    if neighbor not in visits:
                        q.append(neighbor)
                        visits.add(neighbor)
            length+=1

        for val, node in adjList.items():
            i=0
            for neighbor_val in node.neighbors:
                node.neighbors[i] = adjList[neighbor_val]
                i+=1
        return new_node_1


        