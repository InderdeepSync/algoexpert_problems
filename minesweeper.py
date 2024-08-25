def getNeighbors(board, row, col):
    result = []

    for i in [row - 1, row, row + 1]:
        for j in [col - 1, col, col + 1]:
            if 0 <= i <= len(board) - 1 and 0 <= j <= len(board[0]) - 1:
                if i == row and j == col:
                    continue

                result.append((i, j))

    return result


def inner(board, row, column, visited):
    visited.add((row, column))
    if board[row][column] == "M" and len(visited) == 1:
        board[row][column] = "X"

    elif board[row][column] == "H":
        neighbors = getNeighbors(board, row, column)
        print("Neighbors", neighbors)
        mineCount = list(map(lambda n: board[n[0]][n[1]], neighbors)).count("M")
        board[row][column] = str(mineCount)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            inner(board, *neighbor, visited)

    return board


def revealMinesweeper(board, row, column):
    return inner(board, row, column, set())


if __name__ == "__main__":
    print(revealMinesweeper([
    ["H", "M"],
    ["H", "H"]
  ], 1, 1))