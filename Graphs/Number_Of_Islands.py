#For every piece of land we have not seen aka when we come across and new "1". We run bfs to find the size of that island. 
#pseudocode:
#visited =set()
#for row in grid:
    #for col in row:
        #if grid[row][col] == "1" and not in visited:
            #run bfs(row, col)
            #islands +=1
#return islands
#complexity when we run bfs we can at most look throguh every row and col O(m * n) 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions=[[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            while q:
                curr = q.pop()
                visited.add((r, c))
                for d in directions:
                    currR = curr[0] + d[0]
                    currC = curr[1] + d[1]
                    if currR < 0 or currR >= rows or currC < 0 or currC >= cols or (currR, currC) in visited or grid[currR][currC] == "0":
                        continue

                    q.append((currR, currC))
                    visited.add((currR, currC))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands +=1
        return islands
                


