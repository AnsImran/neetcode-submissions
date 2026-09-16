# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val  = val
#         self.next = next

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

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next:
                prev, current = None, head
                if head.next.next:
                    nex = head.next.next
                else:
                    nex = None
                while current:
                    if current.next:
                        nex = current.next
                    else:
                        nex = None
                    current.next = prev
                    prev         = current
                    current      = nex
                return prev
            else:
                return head
        else:
            return
































        



        
































        



        