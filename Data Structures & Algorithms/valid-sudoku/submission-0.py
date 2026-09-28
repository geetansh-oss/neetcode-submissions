from collections import defaultdict 

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        mapRow = defaultdict(set)
        mapCol = defaultdict(set)
        mapSubMatrix = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in mapRow[r] or 
                    board[r][c] in mapCol[c] or 
                    board[r][c] in mapSubMatrix[(r//3, c//3)]):
                    return False
                else:
                    mapRow[r].add(board[r][c])
                    mapCol[c].add(board[r][c])
                    mapSubMatrix[(r//3, c//3)].add(board[r][c])

        return True
        