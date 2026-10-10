class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        out = 0
        visited = set() 
        if not grid:
            return 0

        def bfs(i,j):
            p = collections.deque()
            visited.add((i,j))
            p.append((i,j))
            while p:
                r,c = p.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for d in directions:
                    if r + d[0] in range(len(grid))and c+d[1] in range(len(grid[0]))and grid[r][c] == "1"and (r+d[0],c+d[1]) not in visited:
                        visited.add((r+d[0],c+d[1]))
                        p.append((r+d[0],c+d[1]))


        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    out+=1
                    bfs(i,j)
        return out