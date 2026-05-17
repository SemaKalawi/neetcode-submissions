class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #swap elements across main diagonal (i,j) -> (j,i)
        n = len(matrix)
        rotation = [[0] * n for _ in range(n)] #new matrix where each element from og matrix is in rotated position

        for i in range(n):
            for j in range(n):
                rotation[j][n-1-i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotation[i][j]

        