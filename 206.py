# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        itr = head
        temp = ListNode()
        while itr != None:
            temp.val = itr.val
            if itr.next != None:
                temp2 = ListNode()
                temp2.next = temp
                temp = temp2
            itr = itr.next 
        return temp
