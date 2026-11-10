#Clarification: at the beggining of the traversal should we assume only one fruit is rotten?
#minimum number of minutes = depth? -> need levels bc we can start with many rotting fruits
#We add all rotten fruits to the queue before running BFS (level traversal)
#Pseudocode
#find rotten fruits and add to queue
#BFS:
    #check every direction make sure we have not visited
    #we need to split by levels we need to pop every curr element in queue before moving on to next level 
    #minute +=1
#O(m*n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        visited=set()
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        #figure out how many minutes (BFS)
        def bfs(q):
            mins = 0
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                elemToPop = len(q)
                for e in range(elemToPop):
                    currF = q.popleft()
                    visited.add((currF[0], currF[1]))
                    for d in directions:
                        currR = currF[0] + d[0]
                        currC = currF[1] + d[1]
                        if currR < 0 or currR >= rows or currC < 0 or currC >= cols or (currR, currC) in visited or grid[currR][currC] == 0 or grid[currR][currC] == 2:
                            continue
                        q.append((currR, currC))
                        visited.add((currR, currC))
                        grid[currR][currC] = 2
                mins+=1 
            #at level 0 no minutes have passed  
            return mins-1
        #find rotten fruits 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        if q:
            minutes = bfs(q)
        #check to make sure no fresh fruits remain
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    minutes = -1
        return minutes
