class MarkovianPriorityMatcher(object):

    @classmethod
    def match(cls, rankingMatrix, stationaryState):
        rankedStationary = sorted(
            enumerate(stationaryState), key=lambda s: s[1], reverse=True)

        print(rankedStationary)

        pairs = []
        taken = {i: False for i in cls.__getRankingRange(rankingMatrix)}

        for index, weight in rankedStationary:
            if taken[index]:
                continue

            rankedPreference = sorted(
                enumerate(rankingMatrix[index]), key=lambda s: s[1] if s[0] != index else len(rankingMatrix), reverse=False)

            firstAvailable = next(
                filter(lambda p: cls.__isAvailable(p, taken), rankedPreference))[0]

            taken[index] = True
            taken[firstAvailable] = True

            pairs.append((index, firstAvailable))

        return pairs

    @classmethod
    def __getRankingRange(cls, rankingMatrix):
        return range(len(rankingMatrix))

    @classmethod
    def __isAvailable(cls, preference, taken):
        prefIndex, prefRanking = preference

        return not taken[prefIndex]
