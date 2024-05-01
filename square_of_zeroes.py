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


def squareOfZeroes(matrix): # Verified on AlgoExpert
    zerosCount = [[[1, 1] if matrix[i][j] == 0 else [0, 0] for j in range(len(matrix[0]))] for i in range(len(matrix))]

    for i in range(len(matrix) - 2, -1, -1):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                continue
            zerosCount[i][j][0] += zerosCount[i + 1][j][0]

    for j in range(len(matrix[0]) - 2, -1, -1):
        for i in range(len(matrix)):
            if matrix[i][j] == 1:
                continue
            zerosCount[i][j][1] += zerosCount[i][j + 1][1]

    for k in range(2, len(matrix) + 1):
        for i in range(0, len(matrix) - (k - 1)):
            for j in range(0, len(matrix) - (k - 1)):
                num1, num2 = zerosCount[i][j]
                _, num3 = zerosCount[i + (k - 1)][j]
                num4, _ = zerosCount[i][j + (k - 1)]
                if num1 >= k and num2 >= k and num3 >= k and num4 >= k:
                    return True

    print(zerosCount)
    return False


if __name__ == "__main__":
    input_matrix = [[1, 1, 0, 1, 0],
                    [1, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0],
                    [1, 1, 0, 1, 0],
                    [1, 0, 0, 0, 0]]
    input_matrix2 = [
        [0, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 1]
      ]
    # pp("Square of Zeroes: {}".format(square_of_zeroes(input_matrix)))
    print(squareOfZeroes(input_matrix2))
