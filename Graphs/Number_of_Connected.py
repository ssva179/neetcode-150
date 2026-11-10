#O(V+E)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dictionary = {}
        for i in range(n):
            dictionary[i] =[]
        for edge in edges:
            dictionary[edge[0]].append(edge[1])
            dictionary[edge[1]].append(edge[0])
        
        def dfs(n):
            neighbors = dictionary[n]
            visited.add(n)
            if not neighbors:
                return
            for m in neighbors:
                if m not in visited:
                    visited.add(m)
                    dfs(m)
                
        visited = set()
        sets = 0
        

        for n in dictionary:
            if n in visited:
                continue
            dfs(n)
            sets +=1
        return sets

