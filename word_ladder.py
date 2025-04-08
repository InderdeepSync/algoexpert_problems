class Solution(object):

    def create_map(self, wordList):
        info = {}
        for word in wordList:
            w_l = list(word)
            for i in range(len(word)):
                temp = w_l[i]
                w_l[i] = '*'
                key = "".join(w_l)
                if key not in info:
                    info[key] = {word}
                else:
                    info[key].add(word)

                w_l[i] = temp

        return info

    def get_neighbors(self, cur):
        result = set()

        for i in range(0, len(cur)):
            cur_l = list(cur)
            cur_l[i] = "*"
            key = "".join(cur_l)
            result = result.union(self.wordMap.get(key, set()))

        if cur in result:
            result.remove(cur)
        result = result.difference(self.visited)
        return result

    def ladderLength(self, beginWord, endWord, wordList): # Verified on Leetcode
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        queue = [(beginWord, 1)]
        self.visited = {beginWord}
        self.wordList = wordList
        self.wordMap = self.create_map(wordList)

        while queue:
            (el, count) = queue.pop(0)
            neighbors = self.get_neighbors(el)
            for n in neighbors:
                if n == endWord:
                    return count + 1
                queue.append((n, count + 1))
                self.visited.add(n)
        return 0

if __name__ == "__main__":
    print(Solution().ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))