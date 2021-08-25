def river_sizes(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    visited = set()

    def should_explore(row_idx, col_idx):
        return 0 <= row_idx < num_rows and 0 <= col_idx < num_columns and matrix[row_idx][col_idx] != 0 and (
            row_idx, col_idx) not in visited

    def find_river(row_index, col_index):
        visited.add((row_index, col_index))

        river_length = 1
        if should_explore(row_index - 1, col_index):
            river_length += find_river(row_index - 1, col_index)
        if should_explore(row_index + 1, col_index):
            river_length += find_river(row_index + 1, col_index)
        if should_explore(row_index, col_index - 1):
            river_length += find_river(row_index, col_index - 1)
        if should_explore(row_index, col_index + 1):
            river_length += find_river(row_index, col_index + 1)

        return river_length

    river_sizes_arr = []
    for i in range(num_rows):
        for j in range(num_columns):
            if should_explore(i, j):
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
