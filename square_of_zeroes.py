from pprint import pprint as pp

def square_of_zeroes(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    max_square_edge_length = min(num_rows, num_columns) - 1
    data = [[(0, 0) for _ in range(num_columns + 1)] for _ in range(num_rows + 1)]
    for index1 in reversed(range(num_rows)):
        for index2 in reversed(range(num_columns)):
            if matrix[index1][index2] == 1:
                data[index1][index2] = (0, 0)
                continue

            data[index1][index2] = (data[index1 + 1][index2][0] + 1, data[index1][index2 + 1][1] + 1)

    for i in range(num_rows):
        for j in range(num_columns):
            for size in range(1, max_square_edge_length + 1):
                if i + size < num_rows and j + size < num_columns:
                    if data[i][j][0] >= size + 1 and data[i][j][1] >= size + 1 and data[i + size][j][1] >= size + 1 and data[i][j + size][0] >= size + 1:
                        return (i, j), size

    return None


if __name__ == "__main__":
    input_matrix = [[1, 1, 0, 1, 0],
                    [1, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 0, 1, 0],
                    [1, 0, 0, 0, 0]]
    pp("Square of Zeroes: {}".format(square_of_zeroes(input_matrix)))