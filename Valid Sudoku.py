from typing import List


class Solution:

    def validator(self, board: List[List[str]], x, y) -> bool:
        map = {}
        for i in range(0 + x, x + 3):
            for j in range(0 + y, y + 3):

                val = board[i][j]
                if val in map:
                    return False
                if val >= "1" and val <= "9":
                    map[val] = val
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if self.validator(board, i, j) == False:
                    return False

        for i in range(0, 9):
            colMap = {}
            rowMap = {}
            for j in range(0, 9):

                cVal = board[i][j]
                if cVal in colMap:
                    return False
                elif cVal >= "1" and cVal <= "9":
                    colMap[cVal] = cVal

                rVal = board[j][i]
                if rVal in rowMap:
                    return False
                elif rVal >= "1" and rVal <= "9":
                    rowMap[rVal] = rVal

        return True


print(
    Solution().isValidSudoku(
        [
            ["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)

print(
    Solution().isValidSudoku(
        board=[
            [".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )
)
