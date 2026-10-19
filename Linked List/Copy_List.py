"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#pseudocode
#intialize dict
#while curr:
    #copy node
    #add copy to dict
    #curr = curr.next
#cur = head
#while curr:
    #copy = dict[curr]
    #copy.next = curr.next
    #copy.random = curr.random
    #curr = curr.next
#return dict[head]
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        store = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            store[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = store[curr]
            copy.next = store[curr.next]
            copy.random = store[curr.random]
            curr = curr.next
        return store[head]
