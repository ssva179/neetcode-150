#start traversing from border for every 0 we run bfs, we keep track of nodes that are reachable from border. 
#we re traverse through the board marking any nodes not in visited as x
#O(m*n)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                curr = q.pop()
                for d in directions:
                    currR = curr[0] + d[0]
                    currC = curr[1] + d[1]
                    if currR < 0 or currR >= rows or currC < 0 or currC >= cols or board[currR][currC] == "X" or (currR, currC) in visited:
                        continue
                    visited.add((currR,currC))
                    q.append((currR, currC))


        #checking for O's in border and running bfs
        for r in range(rows):
            if r == 0 or r == rows-1:
                for c in range(cols):
                    if board[r][c] == "O":
                        bfs(r, c)
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols-1] == "O":
                bfs(r, cols-1)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"

        
