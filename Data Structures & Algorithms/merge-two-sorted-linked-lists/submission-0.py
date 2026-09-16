# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1:
            head1  = list1
        else:
            head1 = None
        if list2:
            head2 = list2
        else:
            head2  = None

        if head1 == None and head2 == None:
            return None
        else:
            if head2 == None:
                merged    = head1
                main_head = merged
                if head1.next:
                    head1 = head1.next
                else:
                    head1 = None

            elif head1 == None:
                merged    = head2
                main_head = merged
                if head2.next:
                    head2 = head2.next
                else:
                    head2 = None

            elif head1.val <= head2.val:
                merged      = head1
                main_head   = merged
                # merged.next = head2
                # merged      = merged.next
                if head1.next:
                    head1 = head1.next
                else:
                    head1 = None
                # if head2.next:
                #     head2 = head2.next
                # else:
                #     head2 = None
            elif head1.val > head2.val:
                merged      = head2
                main_head   = merged
                # merged.next = head1
                # merged      = merged.next
                # if head1.next:
                #     head1 = head1.next
                # else:
                #     head1 = None
                if head2.next:
                    head2 = head2.next
                else:
                    head2 = None
            
            

            while head1 or head2:
                if head2 == None:
                    merged.next = head1
                    merged      = merged.next
                    if head1.next:
                        head1 = head1.next
                    else:
                        head1 = None
                elif head1 == None:
                    merged.next = head2
                    merged      = merged.next
                    if head2.next:
                        head2 = head2.next
                    else:
                        head2 = None


                elif head1.val <= head2.val:
                    merged.next      = head1
                    # merged.next.next = head2
                    # merged           = merged.next.next
                    merged           = merged.next
                    if head1.next:
                        head1 = head1.next
                    else:
                        head1 = None
                    # if head2.next:
                    #     head2 = head2.next
                    # else:
                    #     head2 = None
                elif head1.val > head2.val:
                    merged.next      = head2
                    # merged.next.next = head1
                    # merged           = merged.next.next
                    merged           = merged.next
                    # if head1.next:
                    #     head1 = head1.next
                    # else:
                    #     head1 = None
                    if head2.next:
                        head2 = head2.next
                    else:
                        head2 = None
            return main_head










        





