

def longest_balanced_substring(string):  # TODO Refer to Alternate optimal approach too
    stack = [-1]
    max_length = 0
    for index, char in enumerate(string):
        if char == "(":
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                stack.append(index)
            else:
                max_length = max(max_length, index - stack[-1])
    return max_length


if __name__ == "__main__":
    print("Longest Balanced Substring: {}".format(longest_balanced_substring("(()))(")))