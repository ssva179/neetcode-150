# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Idea: start at each head compare both vals continue to iterate until we reach the end of one list then append the rest of the second list
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        newlist = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                newlist.next = list1
                list1 = list1.next
            elif list1.val >= list2.val:
                newlist.next = list2
                list2 = list2.next
            newlist = newlist.next
        if list1:
            newlist.next = list1
        if list2:
            newlist.next= list2
        return dummy.next
