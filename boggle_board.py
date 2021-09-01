from suffix_tree import SuffixTree


def boggle_board(board, words):
    num_rows = len(board)
    num_columns = len(board[0])

    def get_allowed_neighbours(coords, visited):
        def is_valid_cell(row_index, col_index):
            return 0 <= row_index < num_rows and 0 <= col_index < num_columns and (row_index, col_index) not in visited

        row_idx, col_idx = coords
        if is_valid_cell(row_idx + 1, col_idx):
            yield row_idx + 1, col_idx
        if is_valid_cell(row_idx - 1, col_idx):
            yield row_idx - 1, col_idx
        if is_valid_cell(row_idx, col_idx + 1):
            yield row_idx, col_idx + 1
        if is_valid_cell(row_idx, col_idx - 1):
            yield row_idx, col_idx - 1
        if is_valid_cell(row_idx + 1, col_idx + 1):
            yield row_idx + 1, col_idx + 1
        if is_valid_cell(row_idx - 1, col_idx - 1):
            yield row_idx - 1, col_idx - 1
        if is_valid_cell(row_idx - 1, col_idx + 1):
            yield row_idx - 1, col_idx + 1
        if is_valid_cell(row_idx + 1, col_idx - 1):
            yield row_idx + 1, col_idx - 1

    def find_words_starting_at(x_coord, y_coord):
        queue = [{"coordinate": (x_coord, y_coord), "visited_till_now": set(), "sub_tree": tree}]
        while queue:
            node = queue.pop(0)
            row_index, col_index = node["coordinate"]
            current_char = board[row_index][col_index]

            sub_tree = node["sub_tree"].get_child_with_char(current_char)
            if not sub_tree:
                continue

            for child_node in sub_tree.children:
                if child_node.char == "*":
                    words_found.add(child_node.word_formed)
                    break

            neighbours = get_allowed_neighbours(node["coordinate"], node["visited_till_now"])
            for neighbour in neighbours:
                temp = set(node["visited_till_now"])
                temp.add(node["coordinate"])
                queue.append({"coordinate": neighbour, "visited_till_now": temp, "sub_tree": sub_tree})

    tree = SuffixTree(char="/", children=[])
    for word in words:
        tree.add_suffix_to_tree(word)

    words_found = set()
    for i in range(num_rows):
        for j in range(num_columns):
            find_words_starting_at(i, j)

    return words_found


if __name__ == "__main__":
    input_board = [["o", "a", "b", "n"],
                   ["o", "t", "h", "e"],
                   ["a", "m", "k", "r"],
                   ["a", "f", "l", "v"]]
    words_list = ["oa", "oat", "oath"]

    input_board2 = [["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                    ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]]
    words_list2 = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]

    input_board3 = [["t", "h", "i", "s", "i", "s", "a"],
                    ["s", "i", "m", "p", "l", "e", "x"],
                    ["b", "x", "x", "x", "x", "e", "b"],
                    ["x", "o", "g", "g", "l", "x", "o"],
                    ["x", "x", "x", "D", "T", "r", "a"],
                    ["R", "E", "P", "E", "A", "d", "x"],
                    ["x", "x", "x", "x", "x", "x", "x"],
                    ["N", "O", "T", "R", "E", "-", "P"],
                    ["x", "x", "D", "E", "T", "A", "E"], ]
    words_list3 = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]
    print("Boggle Board: {}".format(boggle_board(input_board3, words_list3)))
