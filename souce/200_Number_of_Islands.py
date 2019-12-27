'''
Overview:
    
    Given a 2d grid map of '1's (land) and '0's (water), count the number of blocks of '1's.

Solution:

    DFS
'''

class Solution:
    walk = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res;
    
    def dfs(self, grid, x, y):
        grid[x][y] = '#'
        for i in range(4):
            a = x + self.walk[i][0]
            b = y + self.walk[i][1]
            if a < 0 or a >= len(grid) or b < 0 or b >= len(grid[a]) or grid[a][b] != '1':
                continue
            self.dfs(grid, a, b)
