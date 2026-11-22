class Solution:
    def solveSudoku(self, board):
        rows = []
        cols = []
        boxes = []
        for i in range(9):
            rows.append(set())
            cols.append(set())
            boxes.append(set())

        empties = []

        # 1. Mundu unna numbers anni sets lo vey + khali cells list chey
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        # 2. Backtracking - empties list meedha matrame
        def solve(idx):
            if idx == len(empties):
                return True

            r, c = empties[idx]
            box_id = (r // 3) * 3 + (c // 3)

            for num in ['1','2','3','4','5','6','7','8','9']:
                # O(1) check - scan cheyakkarledu
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                    # Petti, sets lo add chey
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)

                    if solve(idx + 1):
                        return True

                    # Backtrack - teesi, sets nunchi kuda teesey
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_id].remove(num)

            return False

        solve(0)