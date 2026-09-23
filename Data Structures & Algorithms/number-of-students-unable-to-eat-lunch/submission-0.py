class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.val  = val
    
def _array_to_linked_list(  dummy_head:Node, 
                            dummy_tail:Node,
                            students  :List[int]
                            ):
    c=0
    prev_node = dummy_head
    for i in students:
        current_node   = Node(i, None, None)

        prev_node.next    = current_node
        current_node.prev = prev_node 
        
        prev_node = current_node
        c        += 1

    dummy_tail.prev   = current_node
    current_node.next = dummy_tail
    student_size      = c

    return dummy_head, dummy_tail, student_size

def _remove_from_top(dummy_head:Node):
    top_node = dummy_head.next
    new_top  = top_node.next

    dummy_head.next = new_top
    new_top.prev    = dummy_head

    top_node.next = None
    top_node.prev = None
    old_top       = top_node
    return dummy_head, old_top

def _shift_to_end(dummy_head:Node, dummy_tail:Node):
    dummy_head, new_end_node = _remove_from_top(dummy_head)

    old_end_node = dummy_tail.prev

    old_end_node.next = new_end_node
    new_end_node.next = dummy_tail
    dummy_tail.prev   = new_end_node
    new_end_node.prev = old_end_node
    return dummy_head, dummy_tail


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        dummy_head = Node(0, None, None)
        dummy_tail = Node(0, None, None)

        dummy_head.next = dummy_tail # Helps when only 1 student
        dummy_tail.prev = dummy_head

        dummy_head, dummy_tail, students_size = _array_to_linked_list(dummy_head, dummy_tail, students)

        for sandwich in sandwiches:
            count        = 1
            while count <= students_size:
                current_node = dummy_head.next
                # match branch
                if sandwich == current_node.val:
                    dummy_head, _  = _remove_from_top(dummy_head)
                    students_size -= 1
                    count          = students_size+1
                    if students_size == 0:
                        return 0
                    else:
                        continue
                else:
                    dummy_head, _ = _shift_to_end(
                                                    dummy_head,
                                                    dummy_tail
                                                )
                    count += 1
                    if count > students_size:
                        return students_size
                    else:
                        continue





        


        














        