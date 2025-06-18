class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            for i in range(len(matrix)):
                for j in range(i+1,len(matrix)):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        def reverse_rows(matrix):
            for i in range(len(matrix)):
                matrix[i].reverse()
        transpose(matrix)
        reverse_rows(matrix)

        
        
