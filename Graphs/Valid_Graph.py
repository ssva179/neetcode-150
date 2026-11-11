#we run dfs if we come across a node we already visited we return false bc this means there is a cycle
#Keep track of parent to account for undirected graph
#O(V+E)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dictionary = {}
        for i in range(n):
            dictionary[i] =[]
        for edge in edges:
            dictionary[edge[0]].append(edge[1])
            dictionary[edge[1]].append(edge[0])
        visited = set()

        def dfs(n, parent):
            if n in visited:
                return False
            
            visited.add(n)
            for neighbor in dictionary[n]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, n):
                    return False
            return True
        #returns false for disconnected graphs
        return dfs(0, -1) and len(visited)==n
                        


        
        
