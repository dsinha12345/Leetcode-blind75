class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            max_path = 1

            d = [(-1,0),(0,1),(1,0),(0,-1)]
            for dx,dy in d:
                di, dj  = i+dx,j+dy
                if 0<=di<rows and 0<=dj<cols and matrix[di][dj]>matrix[i][j]:
                    max_path = max(max_path,1+dfs(di,dj))
            
            memo[(i,j)] = max_path
            return memo[(i,j)]

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c))
                
        return longest
# i don remember this
