#union find: find-> checks if node in a set, merge-> joins two sets together
#One by one add all edges if adding an edge == cycle we return that edge
#if adding an edge connects two nodes already in same set
#same parent idea [flat tree] if two nodes have the same parent == cycle
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #set each nodes parents to itself
        parent = [i for i in range(len(edges)+1)]
        rank = [1] *(len(edges)+1)

        def find(n):
            #will go up until we reach the root
            if parent[n] == n:
                return n 
            parent[n] = find(parent[n])
            return parent[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
