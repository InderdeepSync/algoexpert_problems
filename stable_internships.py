
def stableInternships(interns, teams):
    result = []
    internsMatched = set()

    for teamIdx, team in enumerate(teams):
        print("Interns => ", interns, "Teams =>", teams)
        p = {}
        for internIdx, intern in enumerate(interns):
            if internIdx in internsMatched:
                continue
            if intern.index(teamIdx) not in p:
                p[intern.index(teamIdx)] = [internIdx]
            else:
                p[intern.index(teamIdx)].append(internIdx)

        internsInterested = p[min(p.keys())]
        bestMatch = internsInterested[0]
        if len(internsInterested) == 1:
            internsMatched.add(internsInterested[0])
            result.append([internsInterested[0], teamIdx])
        else:
            for interestedIntern in internsInterested[1:]:
                if team.index(interestedIntern) < team.index(bestMatch):
                    bestMatch = interestedIntern

            internsMatched.add(bestMatch)
            result.append([bestMatch, teamIdx])
        print("Match => ", (bestMatch, teamIdx))
        del interns[bestMatch]
        for intern in interns:
            intern.remove(teamIdx)
            for idx, _ in enumerate(intern):
                if intern[idx] > teamIdx:
                    intern[idx] -= 1

        del teams[teamIdx]
        for teamx in teams:
            teamx.remove(bestMatch)
            for tdx, _ in enumerate(teamx):
                if teamx[tdx] > bestMatch:
                    teamx[tdx] -= 1

    return result


if __name__ == "__main__":
    print(stableInternships([
      [0, 1, 2],
      [0, 2, 1],
      [1, 2, 0]
    ], [
      [2, 1, 0],
      [0, 1, 2],
      [0, 2, 1]
    ]))