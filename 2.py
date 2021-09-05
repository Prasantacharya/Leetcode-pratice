# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        itr = output
        carry = 0
        while(l1 != None or l2 != None):
            if (l1 != None and l2 != None):
                itr.val = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10
            else:
                if l1 != None:
                    itr.val = (l1.val + carry) % 10
                    carry = (l1.val + carry) // 10
                else:
                    itr.val = (l2.val + carry) % 10
                    carry = (l2.val + carry) // 10
            if ((l1 and l1.next != None) or (l2 and l2.next != None)):
                itr.next = ListNode()
                itr = itr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry > 0:
            itr.next = ListNode(1)
        return output
