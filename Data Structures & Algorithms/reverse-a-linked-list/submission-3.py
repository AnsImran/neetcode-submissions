# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head:
#             if head.next:
#                 temp_list=[]
#                 temp_list.append(head)
#                 while head.next:
#                     head = head.next
#                     temp_list.append(head)
#                 for i in range(-1, -len(temp_list) - 1, -1):
#                     head = temp_list[i]
#                     if i >= -1*len(temp_list) + 1:
#                         i = i-1
#                         head.next = temp_list[i]
#                     elif i < -1*len(temp_list) + 1:
#                         head.next = None
#                 return temp_list[-1]
#             else:
#                 return head
#         else:
#             return


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val  = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head:
#             if head.next:
#                 prev, current = head, head.next
#                 if head.next.next:
#                     nex = head.next.next
#                 else:
#                     nex = None
#                 prev.next     = None
#                 while current:
#                     if current.next:
#                         nex = current.next
#                     else:
#                         nex = None
#                     current.next = prev
#                     prev         = current
#                     current      = nex
#                 return prev
#             else:
#                 return head
#         else:
#             return

# Via recursion
def _reverse_the_linked_list(prev, curr, next):
    curr.next = prev
    prev      = curr
    curr      = next
    next      = next.next
    if not next:
        curr.next = prev
        return curr
    else:
        return _reverse_the_linked_list(prev, curr, next)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head:
            if head.next:
                dummy_head = ListNode(0, head)
                prev       = dummy_head        # remember to cutt it off
                curr       = head
                next       = head.next

                original_first_node = curr

                new_head = _reverse_the_linked_list(prev, curr, next)

                original_first_node.next = None

                return new_head

            else:
                return head
        else:
            return
































        



        
































        



        