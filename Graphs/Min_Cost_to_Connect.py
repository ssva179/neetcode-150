#we can use an MST algorithm to find the shortest path connecting all nodes
#Prims
#use pq to store distances continue until all are connected then just calculate the costs of included nodes?
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        totalDist = 0
        visited = set()
        pq = []
        x, y = points[0]
        heapq.heappush(pq, (0, x, y))
        while pq and len(visited)<len(points):
            d, xi, yi = heapq.heappop(pq)
            if (xi, yi) in visited:
                continue
            totalDist += d
            visited.add((xi, yi))
            for nx, ny in points:
                if (nx, ny) in visited:
                    continue
                currD = abs(xi - nx)+abs(yi - ny)
                heapq.heappush(pq, (currD, nx, ny))
        return totalDist


        
