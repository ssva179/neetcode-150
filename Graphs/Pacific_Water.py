#clarify: water can flow to neighboring cells if neighboring height <=  currHeight and all cells flow into the ocean
#we can check which cells will make it to the paciifc and we store in set then we check which ones will make it to the atlantic. The cells that over lap will be the set of our solution
#O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        rows, cols = len(heights), len(heights[0]) 
        res = []

        def bfs(r, c, ocean):
            q = deque()
            q.append((r, c))
            ocean.add((r,c))
            while q:
                curr = q.pop()
                for d in directions:
                    currR = curr[0] + d[0]
                    currC = curr[1] + d[1]
                    if currR < 0 or currR >= rows or currC < 0 or currC >= cols or heights[curr[0]][curr[1]] > heights[currR][currC] or (currR, currC) in ocean:
                        continue
                    q.append((currR, currC))
                    ocean.add((currR, currC))

        #check pacific
        for r in range(rows):
            if r == 0:
                for c in range(cols):
                    bfs(r, c, pacific)
            bfs(r, 0, pacific)
        #check atlantic
        for r in range(rows):
            if r == rows-1:
                for c in range(cols):
                    bfs(r, c, atlantic)
            bfs(r, cols-1, atlantic)
        for pair in pacific:
            if pair in atlantic:
                res.append([pair[0], pair[1]])
        return res

        
