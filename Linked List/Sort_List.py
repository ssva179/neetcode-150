
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Clarify: We have to sort a linked list without using additional storage
#Brute: Keep iterating through array until its all sorted like bubblesort O(n^2)
#optimize: we can optimize space by using a more efficient algorithm like merge sort
#we continuously split the array and merge up recursively with the lists already beying sorted O(n log n) we iterate once to find the middle then we merge recursively

#pseudocode:
    #base case 
        #if one node left or none
            #return node
    #split into two lists
    #return merged(list1, list two)

    
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        left = head
        right = None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow

        tmp = right.next
        right.next = None
        right = tmp
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeTwoLists(left, right)


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
