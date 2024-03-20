class SuffixTrie:
    def __init__(self, words):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(words)

    def _addString(self, string):
        i = 0
        cur = self.root
        while i < len(string):
            if string[i] not in cur:
                cur[string[i]] = {}

            cur = cur[string[i]]
            i += 1

        cur["*"] = string

    def populateSuffixTrieFrom(self, words):
        for word in words:
            self._addString(word)

    def contains(self, string):
        cur = self.root
        i = 0
        while True:
            if i == len(string):
                return "*" in cur
            if string[i] not in cur:
                return False

            cur = cur[string[i]]
            i += 1


def getNeighbors(i, j, board, visited):
    result = [(i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1), (i + 1, j + 1), (i, j + 1), (i, j - 1), (i - 1, j),
              (i + 1, j)]
    condition = lambda c: 0 <= c[0] < len(board) and 0 <= c[1] < len(board[0]) and c not in visited
    return list(filter(condition, result))


def traverse(cur, i, j, board, visited):
    words_found = set()

    if board[i][j] not in cur:
        return words_found

    if "*" in cur[board[i][j]]:
        words_found.add(cur[board[i][j]]["*"])

    visited.add((i, j))

    for neighbor in getNeighbors(i, j, board, visited):
        temp = traverse(cur[board[i][j]], *neighbor, board, visited=set(visited))
        words_found = words_found.union(temp)

    return words_found


def boggleBoard(board, words):  # Verified on Leetcode
    result = set()
    trie = SuffixTrie(words)
    print(trie.root)
    for i in range(len(board)):
        for j in range(len(board[0])):
            result = result.union(traverse(trie.root, i, j, board, visited=set()))

    return result

if __name__ == "__main__":
    print(boggleBoard([
  ["f", "s", "z"],
  ["t", "e", "i"],
  ["t", "w", "d"]
], ["twisted"]))