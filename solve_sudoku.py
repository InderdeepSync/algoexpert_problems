from pprint import pprint as pp

VALID_DIGITS = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

def solve_sudoku(sudoku):
    def _get_row(coords):
        row_index, _ = coords
        return set(sudoku[row_index])

    def _get_column(coords):
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

    def _get_3_by_3(coords):
        row_index, col_index = coords
        assert 0 <= row_index <= 8 and 0 <= col_index <= 8

        _3_by_3_rows, _3_by_3_cols = _3_by_3_coords(coords)

        _3_by_3 = set()
        for i in range(*_3_by_3_rows):
            for j in range(*_3_by_3_cols):
                _3_by_3.add(sudoku[i][j])

        return _3_by_3

    def _construct_possibilities_hashtable():
        hashtable = {}
        next_pick = []
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                if sudoku[i][j] != "0":
                    continue

                temp1 = VALID_DIGITS - set(filter(lambda x: x != 0, _get_row((i, j))))
                temp2 = VALID_DIGITS - set(filter(lambda x: x != 0, _get_column((i, j))))
                temp3 = VALID_DIGITS - set(filter(lambda x: x != 0, _get_3_by_3((i, j))))

                hashtable[(i, j)] = temp1.intersection(temp2, temp3)
                if len(hashtable[(i, j)]) == 1:
                    next_pick.append((i, j))

        return hashtable, next_pick

    possibilities, coords_to_be_picked = _construct_possibilities_hashtable()

    while coords_to_be_picked:
        coord = coords_to_be_picked.pop(0)
        only_possibility = possibilities[coord].pop()
        sudoku[coord[0]][coord[1]] = only_possibility

        for row in range(9):
            temp_coord = (row, coord[1])
            if temp_coord not in possibilities or temp_coord in coords_to_be_picked:
                continue

            possibilities[temp_coord].discard(only_possibility)
            if len(possibilities[temp_coord]) == 1:
                coords_to_be_picked.append(temp_coord)

        for column in range(9):
            temp_coord = (coord[0], column)
            if temp_coord not in possibilities or temp_coord in coords_to_be_picked:
                continue

            possibilities[temp_coord].discard(only_possibility)
            if len(possibilities[temp_coord]) == 1:
                coords_to_be_picked.append(temp_coord)

        _3_by_3_rows, _3_by_3_cols = _3_by_3_coords(coord)

        for i in range(*_3_by_3_rows):
            for j in range(*_3_by_3_cols):
                if (i, j) not in possibilities or (i, j) in coords_to_be_picked:
                    continue
                possibilities[(i, j)].discard(only_possibility)
                if len(possibilities[(i, j)]) == 1:
                    coords_to_be_picked.append((i, j))


if __name__ == "__main__":
    board = [["5", "3", "0", "0", "7", "0", "0", "0", "0"],
             ["6", "0", "0", "1", "9", "5", "0", "0", "0"],
             ["0", "9", "8", "0", "0", "0", "0", "6", "0"],
             ["8", "0", "0", "0", "6", "0", "0", "0", "3"],
             ["4", "0", "0", "8", "0", "3", "0", "0", "1"],
             ["7", "0", "0", "0", "2", "0", "0", "0", "6"],
             ["0", "6", "0", "0", "0", "0", "2", "8", "0"],
             ["0", "0", "0", "4", "1", "9", "0", "0", "5"],
             ["0", "0", "0", "0", "8", "0", "0", "7", "9"]]

    solve_sudoku(board)
    pp(board)

