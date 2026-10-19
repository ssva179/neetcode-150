# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy 
        curr = l
        while True:
            ith = self.getIth(l, k)
            if not ith:
                break
            groupNxt = ith.next

            prev, curr = ith.next, l.next
            while curr != groupNxt:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr =tmp
            tmp = l.next
            l.next = ith
            l = tmp
        return dummy.next
