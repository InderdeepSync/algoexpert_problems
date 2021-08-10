def river_sizes(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    seen = {(i, j): False for i in range(num_rows) for j in range(num_columns)}

    river_sizes_arr = []

    def find_river(row_index, col_index):
        is_seen = seen[(row_index, col_index)]
        seen[(row_index, col_index)] = True

        if matrix[row_index][col_index] == 0 or is_seen:
            return 0

        river_up = find_river(row_index - 1, col_index) if row_index - 1 >= 0 else 0
        river_down = find_river(row_index + 1, col_index) if row_index + 1 <= num_rows - 1 else 0
        river_left = find_river(row_index, col_index - 1) if col_index - 1 >= 0 else 0
        river_right = find_river(row_index, col_index + 1) if col_index + 1 <= num_columns - 1 else 0

        river_length = 1 + river_right + river_left + river_up + river_down
        return river_length


    for i in range(num_rows):
        for j in range(num_columns):
            if not seen[(i, j)] and matrix[i][j] != 0:
                river_size = find_river(i, j)
                river_sizes_arr.append(river_size)

    return river_sizes_arr


if __name__ == "__main__":
    input_matrix = [[1, 0, 0, 1, 0],
                    [1, 0, 1, 0, 0],
                    [0, 0, 1, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 0]]

    input_matrix2 = [[1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]]
    input_matrix3 = [[1],
                     [1],
                     [1],
                     [0],
                     [1],
                     [0],
                     [1],
                     [1]]
    result = river_sizes(input_matrix)
    print(result)
