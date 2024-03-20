def waterfallStreams(array, source): # Verified on Algoexpert
    result = [0] * len(array[0])
    queue = [(100, (0, source), None)]
    while queue:
        vol, cord, prev = queue.pop(0)
        if cord[0] == len(array) - 1:
            result[cord[1]] += vol
            continue

        if not 0 <= cord[1] < len(array[0]) or array[cord[0]][cord[1]] == 1:
            continue

        if array[cord[0] + 1][cord[1]] == 0:
            queue.append((vol, (cord[0] + 1, cord[1]), cord))
        elif prev is None or prev[0] < cord[0]:
            queue.append((vol / 2, (cord[0], cord[1] + 1), cord))
            queue.append((vol / 2, (cord[0], cord[1] - 1), cord))
        else:
            if cord[1] > prev[1]:
                queue.append((vol, (cord[0], cord[1] + 1), cord))
            else:
                queue.append((vol, (cord[0], cord[1] - 1), cord))

    return list(result)



if __name__ == "__main__":
    print(waterfallStreams([
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0]
  ], 3))