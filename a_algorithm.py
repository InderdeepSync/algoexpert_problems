
def a_algorithm(grid, start, end):
    def _get_allowed_neighbours(coords):
        def is_valid_cell(row_index, col_index):
            return 0 <= row_index < len(grid) and 0 <= col_index < len(grid[0]) and grid[row_index][
                col_index] != 1 and (row_index, col_index) not in visited

        result = []
        row_idx, col_idx = coords
        if is_valid_cell(row_idx + 1, col_idx):
            result.append((row_idx + 1, col_idx))
        if is_valid_cell(row_idx - 1, col_idx):
            result.append((row_idx - 1, col_idx))
        if is_valid_cell(row_idx, col_idx + 1):
            result.append((row_idx, col_idx + 1))
        if is_valid_cell(row_idx, col_idx - 1):
            result.append((row_idx, col_idx - 1))
        return result

    temp = [{"coordinates": start, "distance": 0, "minimum_path": []}]
    visited = set()
    while temp:
        grid_cell = temp.pop(0)
        visited.add(grid_cell["coordinates"])

        updated_minimum_path = grid_cell["minimum_path"] + [grid_cell["coordinates"]]

        if grid_cell["coordinates"] == end:
            return updated_minimum_path

        neighbours = map(lambda n: {"coordinates": n, "distance": grid_cell["distance"] + 1,
                                    "minimum_path": updated_minimum_path},
                         _get_allowed_neighbours(grid_cell["coordinates"]))
        temp.extend(neighbours)

    return float("inf")


if __name__ == "__main__":
    input_grid = [[0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0],
                  [1, 0, 1, 1, 1],
                  [0, 0, 0, 0, 0]]
    print("A* Algorithm: {}".format(a_algorithm(input_grid, start=(0, 1), end=(4, 3))))