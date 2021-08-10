
def spiral_traverse(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    res = []
    while num_rows > 0 and num_columns > 0:
        res.extend(perimeter_func(matrix))
        matrix = _get_inner_matrix(matrix)
        num_rows -= 2
        num_columns -= 2

    return res


def perimeter_func(matrix):
    transpose_matrix = list(zip(*matrix))

    upper_boundary = matrix[0]
    right_boundary = list(transpose_matrix[-1][1:-1])
    lower_boundary = list(reversed(matrix[-1])) if upper_boundary is not matrix[-1] else []
    left_boundary = list(reversed([*transpose_matrix[0][1:-1]]))

    return upper_boundary + right_boundary + lower_boundary + left_boundary


def _get_inner_matrix(matrix):
    return list(map(lambda row: row[1: -1], matrix[1: -1]))




if __name__ == "__main__":
    input_matrix = [[1,  2,  3,  4,  5],
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
    result = spiral_traverse(input_matrix3)
    print(result)