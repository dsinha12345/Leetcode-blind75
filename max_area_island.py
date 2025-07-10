class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        row,col = len(grid),len(grid[0])

        def area(i,j):
            if i<0 or i>row-1 or j<0 or j>col-1 or grid[i][j]==0:
                return 0
            if grid[i][j]==1:
                grid[i][j]=0
                return 1+area(i-1,j)+area(i+1,j)+area(i,j-1)+area(i,j+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    calc_area = area(i,j)
                    max_area = max(max_area,calc_area)
        return max_area
        
