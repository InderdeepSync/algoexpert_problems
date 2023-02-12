def spiral_traverse(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    res = []
    while not matrix:
        res.extend(perimeter_func(matrix))
        matrix = _get_inner_matrix(matrix)

    return res


# Verified on LeetCode
def perimeter_func(matrix):
    transpose_matrix = list(zip(*matrix))

    upper_boundary = matrix[0]
    right_boundary = list(transpose_matrix[-1][1:-1])
    lower_boundary = list(reversed(matrix[-1])) if upper_boundary is not matrix[-1] else []
    left_boundary = list(reversed([*transpose_matrix[0][1:-1]]))
    left_boundary = [] if len(matrix[0]) == 1 else left_boundary

    return upper_boundary + right_boundary + lower_boundary + left_boundary


def _get_inner_matrix(matrix):
    return list(map(lambda row: row[1: -1], matrix[1: -1]))


def spiral_traversal_elegant(matrix):  # Verified on LeetCode
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    row_upper = 0
    row_lower = num_rows - 1

    col_left = 0
    col_right = num_columns - 1
    spiral_result = []
    while row_upper <= row_lower and col_left <= col_right:
        if row_upper == row_lower:
            spiral_result.extend(matrix[row_upper][col_left: col_right + 1])
            break
        elif col_left == col_right:
            for row_index in range(row_upper, row_lower + 1):
                spiral_result.append(matrix[row_index][col_left])
            break

        for i in range(col_left, col_right):
            spiral_result.append(matrix[row_upper][i])
        for i in range(row_upper, row_lower):
            spiral_result.append(matrix[i][col_right])
        for i in range(col_right, col_left, -1):
            spiral_result.append(matrix[row_lower][i])
        for i in range(row_lower, row_upper, -1):
            spiral_result.append(matrix[i][col_left])

        row_upper += 1
        row_lower -= 1

        col_left += 1
        col_right -= 1

    return spiral_result


if __name__ == "__main__":
    input_matrix = [[1, 2, 3, 4, 5],
                    [16, 17, 18, 19, 6],
                    [15, 24, 25, 20, 7],
                    [14, 23, 22, 21, 8],
                    [13, 12, 11, 10, 9]]

    input_matrix2 = [[1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0]]
    input_matrix3 = [[1],
                     [1],
                     [1],
                     [0],
                     [1],
                     [0],
                     [1],
                     [1]]
    result = spiral_traversal_elegant(input_matrix)
    print(result)
