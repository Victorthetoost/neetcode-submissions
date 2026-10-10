class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        points = []

        if not grid:
            return []
        def bfs(points):
            p = collections.deque()
            for o in points:
                p.append((o,0))
            while p:
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                # calculate the distance to 0
                coord,dist = p.popleft()
                x,y = coord
                for c,r in directions:
                    a = x+c
                    b = y+r
                    if a in range(len(grid)) and b in range(len(grid[0])) and grid[a][b] != 0 and grid[a][b] != -1 and grid[a][b] > dist+1:         
                        grid[a][b] = dist+1
                        p.append(((a,b),dist+1))

                # if distance is smaller overwrite, 
                # if valid append distance +1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    points.append((i,j))
        bfs (points)