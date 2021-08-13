res = 0

def remove_islands(matrix): # Verified on LeetCode(Number of Enclaves)
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    edge_rows = (0, len(matrix) - 1)
    edge_columns = (0, len(matrix[0]) - 1)

    connected_to_edge = {}
    for i in range(num_rows):
        for j in range(num_columns):

            if matrix[i][j] == 0:
                is_conn = False
            elif i in edge_rows or j in edge_columns:
                is_conn = True
            else:
                is_conn = None

            connected_to_edge[(i, j)] = is_conn

    def is_connected_to_edge_one(row_index, col_index, currently_processing):
        if (row_index, col_index) in currently_processing:
            return False

        is_connected = connected_to_edge[(row_index, col_index)]
        if isinstance(is_connected, bool):
            return is_connected

        currently_processing.add((row_index, col_index))

        is_right_connected = is_connected_to_edge_one(row_index, col_index + 1, currently_processing)
        is_left_connected = is_connected_to_edge_one(row_index, col_index - 1, currently_processing)
        is_up_connected = is_connected_to_edge_one(row_index - 1, col_index, currently_processing)
        is_down_connected = is_connected_to_edge_one(row_index + 1, col_index, currently_processing)

        is_connected = is_right_connected or is_left_connected or is_up_connected or is_down_connected

        if matrix[row_index][col_index] == 1 and int(is_connected) == 0:
            global res
            print(row_index, col_index)
            res = res + 1

        matrix[row_index][col_index] = int(is_connected)
        return is_connected


    for i in range(1, num_rows - 1):
        for j in range(1, num_columns - 1):
            connected_to_edge[(i, j)] = is_connected_to_edge_one(i, j, set())

    return matrix


if __name__ == "__main__":
    input_matrix = [[1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0, 1],
                    [0, 0, 0, 1, 1, 0],
                    [1, 1, 1, 0, 1, 0],
                    [1, 0, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0, 1]]

    input_matrix2 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]

    res = remove_islands(input_matrix2)
    print("Remove Islands: {}".format(res))