class Solution:
    def isValidSudoku(self, board):
        # 9 rows kosam 9 sets, 9 cols kosam 9 sets, 9 boxes kosam 9 sets
        rows = []
        cols = []
        boxes = []
        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # '.' ante khali cell - skip chey
                if val == '.':
                    continue

                # Ee cell e 3x3 box lo undo kanukko
                # Ex: r=4, c=7 -> (4//3)*3 + 7//3 = 3 + 2 = 5th box
                box_id = (r // 3) * 3 + (c // 3)

                # Ee 3 chotla ekkada aina already unte - Invalid
                if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                    return False

                # Lekapothe ee 3 chotla add chey
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True