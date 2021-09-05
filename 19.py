# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr = head
        stack = []
        while itr:
            stack.append(itr)
            itr = itr.next
        if len(stack) - n == 0:
            temp = head.next
            head.next = None
            return temp
        elif len(stack) == n:
            return None
        elif n == 1:
            stack[len(stack) - 1 - n].next = None
            return head
        stack[len(stack) - 1 - n].next = stack[len(stack) - n + 1]
        return head
