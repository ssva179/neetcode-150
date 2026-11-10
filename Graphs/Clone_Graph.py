"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


#undirected graph: points both directions
#we can use a hash map to reuse "new" nodes already created in order to use the deep copys
#pseudocode:
#hashmap = {}
#def dfs(node):
    #if node already have a copy:
        #return hashmap[node]
    #else -> create new node and add to map
        #new = Node(node.val)
        #add to hash
        #for node node.neighbors:
            #new.neighbors + dfs(node)
        #return new
        
#return dfs(node)
#O(V+E)

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}
        if not node:
            return None
        def dfs(node):
            if node in hashMap:
                return hashMap[node]
            new = Node(node.val)
            hashMap[node] = new
            for n in node.neighbors:
                #will look up copies already made so we dont have to make them many times
                new.neighbors.append(dfs(n))
            return new

        return dfs(node)
        
