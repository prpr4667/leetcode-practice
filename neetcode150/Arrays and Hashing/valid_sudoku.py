def isValidSudoku(board):
    for i in range(len(board)):
        for i in range(len(board[0])):
            if invalidRowCol(board, i, i):
                return False

    for r in range(0, len(board), 3):
        for c in range(0, len(board[0]), 3):
            if invalidGrid(board, r, r + 3, c, c + 3):
                return False

    return True


def invalidGrid(board, rowStart, rowEnd, colStart, colEnd):
    _set = set()
    for r in range(rowStart, rowEnd):
        for c in range(colStart, colEnd):
            if board[r][c] != "." and board[r][c] in _set:
                return True
            _set.add(board[r][c])

    return False


def invalidRowCol(board, row, col):
    _set = set()
    for c in range(len(board[0])):
        if board[row][c] != "." and board[row][c] in _set:
            return True
        _set.add(board[row][c])

    _set = set()
    for r in range(len(board)):
        if board[r][col] != "." and board[r][col] in _set:
            return True
        _set.add(board[r][col])

    return False


board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]
print(isValidSudoku(board))

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(isValidSudoku(board))
