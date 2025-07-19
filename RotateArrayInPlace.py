class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # uses the neat trick tha transposing (Swappig rows and columns) and then reflecting over a vertical line 
        # ( aka reversing the rows ) is equivalent to a 90 degree rotation clockwise.
        n = len(matrix)

        #transpose a square matrix
        for i in range(n):
            for j in range(i, n, 1):  # descend the diagonal
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        # reverse the transpose
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
