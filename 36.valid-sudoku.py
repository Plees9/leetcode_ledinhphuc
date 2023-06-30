#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dig = [str(n) for n in range(1,10)]

        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] in dig and board[i][j] in row:
                    return False
                if board[i][j] in dig and board[i][j] not in row:
                    row.append(board[i][j])

        for j in range(9):
            col = []
            for i in range(9):
                if board[i][j] in dig and board[i][j] in col:
                    return False
                if board[i][j] in dig and board[i][j] not in col:
                    col.append(board[i][j])

        n = [0,3,6]
        for k in n:
            for p in n:
                sqr = []
                for i in range(0+k,3+k):
                    for j in range(0+p, 3+p):
                        if board[i][j] in dig and board[i][j] in sqr:
                            return False
                        if board[i][j] in dig and board[i][j] not in sqr:
                            sqr.append(board[i][j])

        return True     
# @lc code=end

