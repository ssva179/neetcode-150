# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 
        remainder = 0
        while l1 or l2 or remainder:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            add = val1 + val2 + remainder
            remainder = 0
            if add >= 10:
                remainder = 1
                add = add - 10
            curr.next = ListNode(add)
            curr = curr.next
            if l1:
                l1 = l1.next
            else:
                None
            if l2:
                l2 = l2.next
            else:
                None
        return dummy.next
        
