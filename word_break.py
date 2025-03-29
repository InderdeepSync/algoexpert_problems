from functools import lru_cache
from typing import List

def add_word_to_trie(word, trie):
    if len(word) == 0:
        trie['#'] = True
        return

    ch = word[0]
    if ch not in trie:
        trie[ch] = {}
    add_word_to_trie(word[1:], trie[ch])

def construct_trie(words):
    trie = {}
    for word in words:
        add_word_to_trie(word, trie)

    return trie


class Solution: # Verified on LeetCode #139
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = construct_trie(wordDict)

        @lru_cache()
        def inner(word):
            if len(word) == 0:
                return True

            i = 0
            temp = trie
            while i < len(word) and (ch := word[i]) in temp:
                temp = temp[ch]
                i += 1
                if '#' in temp:
                    if inner(word[i:]):
                        res = True
                        break
            else:  # nobreak
                res = False

            return res

        return inner(s)