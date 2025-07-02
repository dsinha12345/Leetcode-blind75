class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row,col = len(board),len(board[0])
        def dfs(i,j,word):
            if len(word)==0:
                return True
            if i<0 or i>row-1 or j<0 or j>col-1 or board[i][j]!=word[0]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            found = ( dfs(i-1,j,word[1:]) or
            dfs(i+1,j,word[1:]) or 
            dfs(i,j-1,word[1:]) or 
            dfs(i,j+1,word[1:]) )

            board[i][j] = temp
            return found



        for i in range(row):
            for j in range(col):
                if dfs(i,j,word):
                    return True
        return False
