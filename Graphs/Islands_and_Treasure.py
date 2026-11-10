#similar to rotten fruits
#add all gates to a queue and at each level see how many new empty rooms can be reached until we have visited all reachable rooms
#O(m*n)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        layer = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        def bfs(q):
            layer = 0
            while q:
                layer += 1
                layerSize = len(q)
                for n in range(layerSize):
                    curr = q.popleft()
                    visited.add(curr)
                    for d in directions:
                        currR = curr[0] + d[0]
                        currC = curr[1] + d[1]
                        if currR < 0 or currR >= rows or currC < 0 or currC >= cols or grid[currR][currC] == -1 or grid[currR][currC] == 0 or (currR, currC) in visited:
                            continue
                        grid[currR][currC] = layer
                        visited.add((currR, currC))
                        q.append((currR, currC))
        return bfs(q)


        
