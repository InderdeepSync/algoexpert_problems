
def waterfall_streams(matrix, current, quantity, visited):
    def _cell_is_unblocked(row, column):
        return row < len(matrix) and 0 <= column < len(matrix[0]) and matrix[row][column] == 0 and (row, column) not in visited

    visited.add(current)
    cur_row, cur_column = current

    if cur_row == len(matrix) - 1:
        return [0] * cur_column + [quantity] + [0] * (len(matrix[0]) - cur_column - 1)

    if _cell_is_unblocked(cur_row + 1, cur_column):
        return waterfall_streams(matrix, (cur_row + 1, cur_column), quantity, visited)

    is_left_unblocked = _cell_is_unblocked(cur_row, cur_column - 1)
    is_right_unblocked = _cell_is_unblocked(cur_row, cur_column + 1)

    should_split_quantity = is_left_unblocked and is_right_unblocked
    updated_quantity = quantity/(2 if should_split_quantity else 1)

    if is_left_unblocked:
        left_result = waterfall_streams(matrix, (cur_row, cur_column - 1), updated_quantity, visited)
    else:
        left_result = [0] * len(matrix[0])

    if is_right_unblocked:
        right_result = waterfall_streams(matrix, (cur_row, cur_column + 1), updated_quantity, visited)
    else:
        right_result = [0] * len(matrix[0])

    result = [left_result[i] + right_result[i] for i in range(len(matrix[0]))]
    return result


if __name__ == "__main__":
    input_matrix = [[0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0]]
    print("Waterfall Streams: {}".format(waterfall_streams(input_matrix, (0, 3), 100, set())))
