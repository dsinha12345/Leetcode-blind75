class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res= []
        row, col = len(board), len(board[0])
        main_node = TrieNode()
        for word in words:
            curr = main_node
            for i in word:
                if i not in curr.children:
                    curr.children[i] = TrieNode()
                curr = curr.children[i]
            curr.isEnd = True

        def search(i,j,node, path):
            if node.isEnd:
                res.append(path)
                node.isEnd = False 

            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == "#":
                return

            ch = board[i][j]
            if ch not in node.children:
                return
            board[i][j] = "#"

            search(i+1,j,node.children[ch],path+ch)
            search(i-1,j,node.children[ch],path+ch)
            search(i,j+1,node.children[ch],path+ch)
            search(i,j-1,node.children[ch],path+ch)

            board[i][j] = ch


        for i in range(row):
            for j in range(col):
                search(i,j,main_node,"")
        return res
