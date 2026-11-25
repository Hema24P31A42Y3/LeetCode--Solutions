class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        
        # Step 1: Transpose - matrix[i][j] <-> matrix[j][i]
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Prathi row ni reverse chey
        for i in range(n):
            matrix[i].reverse()