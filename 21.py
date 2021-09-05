# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        if not l1 and not l2:
            return None
        head = ListNode()
        itr = head
        while (l1 or l2):
            if l1 and l2:
                if l1.val <= l2.val:
                    itr.val = l1.val
                    l1 = l1.next
                elif l2.val < l1.val:
                    itr.val = l2.val
                    l2 = l2.next
            elif l1:
                itr.val = l1.val
                l1 = l1.next
            elif l2:
                itr.val = l2.val
                l2 = l2.next
            
            if l1 or l2:
                itr.next = ListNode()
                itr = itr.next
                
        return head
