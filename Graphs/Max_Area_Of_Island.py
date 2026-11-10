#This one is pretty similar to number of islands we just calculate the max instead of total number of islands
#pseudocode:
#Area = 0
#visited = set()
#for r in row:
    #for c in col:
        #if grid[r][c] == "1" and not in visited:
            #areaOfIsland = bfs(r, c)
            #area = max(area, areaOfIsland)
#return area
#Complexity O(m*n) bfs traversal 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        visited = set()
        cols = len(grid[0])
        rows = len(grid)
        def bfs(r, c):
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            area = 1 #if we enter bfs its bc we found the beggining of an island
            while q:
                #current "node" we check all neighbors to see if they are part of the island
                curr = q.pop()
                for d in directions:
                    #moving in every direction
                    currR = curr[0] + d[0]
                    currC = curr[1] + d[1]
                    if currR < 0 or currR >= rows or currC < 0 or currC >= cols or (currR, currC) in visited or grid[currR][currC] == 0:
                        continue
                    area += 1
                    q.append((currR, currC))
                    visited.add((currR, currC))
            return area
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = bfs(r, c)
                    maxA = max(maxA, currArea)
        return maxA

      
