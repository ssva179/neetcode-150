#Dijstras algorithm to reach bottom corner starting at (0,0)
#chose the shortest node to reach (n, n) return max water level in that path
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        minMax = 0
        heap = [(grid[0][0],0,0)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while heap:
            elev, r, c = heapq.heappop(heap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            minMax = max(minMax, elev)
            if (r, c) == (rows-1, cols-1):
                return minMax
            for d in directions:
                currR = r + d[0]
                currC = c + d[1]
                if currR < 0 or currR >= rows or currC < 0 or currC >= cols or (currR, currC) in visit:
                    continue
                celev = max(elev, grid[currR][currC])
                heapq.heappush(heap, (celev, currR, currC))

        
