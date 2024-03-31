

def inner(durations, stations):
    assert stations > 0
    if len(durations) == 0:
        return []
    if stations == 1:
        return [sum(durations)]
    if stations >= len(durations):
        return durations

    i = 1
    opts = []
    while len(durations) >= i:
        optX = [sum(durations[:i]), *inner(durations[i:], stations - 1)]
        opts.append(optX)
        i += 1

    return min(*opts, key=max)


def optimalAssemblyLine(stepDurations, numStations): # Verified on AlgoExpert
    result = inner(stepDurations, numStations)
    return max(result)


if __name__ == "__main__":
    print(optimalAssemblyLine([1, 2, 3, 4, 5], 3))
    # print(optimalAssemblyLine([30, 30, 45], 2))
