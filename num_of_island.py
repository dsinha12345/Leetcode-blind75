class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row , col = len(grid),len(grid[0])

        total = 0
        def dfs(i,j):
            if i<0 or i>row-1 or j<0 or j>col-1 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

            return True


        for r in range(row):
            for c in range(col):
                if dfs(r,c):
                    total+=1
        return total
