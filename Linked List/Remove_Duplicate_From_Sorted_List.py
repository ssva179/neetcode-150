# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Clarify: We have to remove every duplicate not just the duplicates of a number so if 2 appears twice we have to remove 2 from the list completly
#Edge case: we have to be careful not to go into a null array 
#Brute: keep track of all duplicated on some sort of dictionary then go in again and remove values that show up in hash
#optimize; we can optimize space by just iteratin through list once

#pseudocode:
    #create dummy
    #prev, curr = dummy, head
    #iterate through the list
        #if we have a duplicate
            #while loop and update curr until we dont have duplicate 
        #connect prev 
        #else:
            #move prev bc no dupe
    #reuturn head

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                #got stil here was getting errors but realized i needed to move curr bc after loop curr points to last occurance of duplicate
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next 
        return dummy.next
