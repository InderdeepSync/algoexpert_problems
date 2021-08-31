from pprint import pprint as pp

def longest_string_chain(arr):  # Verified on Leetcode
    sequences = [{"next": None, "length": 1} for _ in arr]
    hashtable = {}

    arr.sort(key=len)
    for index, word in enumerate(arr):
        hashtable[word] = index

    def _longest_string_chain(word_index):
        current_word = arr[word_index]

        for idx in range(len(arr[word_index])):
            smaller_word = current_word[:idx] + current_word[idx+1:]
            if smaller_word in hashtable:
                smaller_word_index = hashtable[smaller_word]
                if sequences[word_index]["length"] > sequences[smaller_word_index]["length"] + 1:
                    continue

                sequences[word_index]["next"] = smaller_word_index
                sequences[word_index]["length"] = sequences[smaller_word_index]["length"] + 1

    for i in range(len(arr)):
        _longest_string_chain(i)

    pp(arr)
    pp(sequences)

    result = []
    temp = sequences.index(max(sequences, key=lambda x: x["length"]))
    while temp is not None:
        result.append(arr[temp])
        temp = sequences[temp]["next"]

    return result


if __name__ == "__main__":
    print(longest_string_chain(["bdca","bda","ca","dca","a"]))
