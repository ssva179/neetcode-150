# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#dummy node to head
#left and right pointer
#the right pointer should be ahead by n nodes
#keep going until r is null
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while n>0 and r:
            r = r.next
            n-=1
        while r:
            l = l.next
            r = r.next
        #deletion
        l.next = l.next.next
        return dummy.next
