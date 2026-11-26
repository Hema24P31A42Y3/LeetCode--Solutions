class Solution:
    def solveNQueens(self, n):
        res = []
        board = [['.'] * n for _ in range(n)]
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        
        def backtrack(row):
            # anni rows lo queen pettam ante solution dorikindi
            if row == n:
                # board ni string list ga marchi save chey
                solution = [''.join(r) for r in board]
                res.append(solution)
                return
            
            for col in range(n):
                # attack avthundi ante skip
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # 1. Pettu
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # 2. Vellu
                backtrack(row + 1)
                
                # 3. Theesey (Backtrack)
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtrack(0)
        return res