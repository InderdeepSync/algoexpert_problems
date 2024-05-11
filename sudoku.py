from pprint import pprint
import copy

VALID_DIGITS = set(range(1, 10))


def _get_row(coords, sudoku):
    row_index, _ = coords
    return set(sudoku[row_index])


def _get_column(coords, sudoku):
    _, col_index = coords
    return {r[col_index] for r in sudoku}


def _3_by_3_coords(coords):
    def _(idx):
        if 0 <= idx <= 2:
            result = (0, 3)
        elif 3 <= idx <= 5:
            result = (3, 6)
        else:
            result = (6, 9)
        return result

    row_idx, col_idx = coords
    return _(row_idx), _(col_idx)


def _get_3_by_3(coords, sudoku):
    row_index, col_index = coords
    assert 0 <= row_index <= 8 and 0 <= col_index <= 8

    _3_by_3_rows, _3_by_3_cols = _3_by_3_coords(coords)

    _3_by_3 = set()
    for i in range(*_3_by_3_rows):
        for j in range(*_3_by_3_cols):
            _3_by_3.add(sudoku[i][j])

    return _3_by_3


def inner(sudoku):
    position = None
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                position = (i, j)
                break

    if not position:
        return sudoku

    allowedValues = VALID_DIGITS - _get_row(position, sudoku) - _get_column(position, sudoku) - _get_3_by_3(position, sudoku)

    for k in range(1, 10):
        if k in allowedValues:
            sudokuCopy = copy.deepcopy(sudoku)
            r, c = position
            sudokuCopy[r][c] = k
            solvedSudoku = inner(sudokuCopy)
            if solvedSudoku:
                return solvedSudoku

    return None


def solveSudoku(sudoku):
    result = inner(sudoku)
    return result


if __name__ == "__main__":
    board = [
      [0, 2, 0, 0, 9, 0, 1, 0, 0],
      [0, 0, 7, 8, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 3, 6, 0],
      [0, 0, 1, 9, 0, 4, 0, 0, 0],
      [0, 0, 0, 6, 0, 5, 0, 0, 7],
      [8, 0, 0, 0, 0, 0, 0, 0, 9],
      [0, 0, 0, 0, 2, 0, 0, 0, 0],
      [7, 0, 0, 0, 0, 0, 0, 8, 5],
      [4, 9, 0, 0, 3, 0, 0, 0, 0]
    ]
    pprint(solveSudoku(board))
