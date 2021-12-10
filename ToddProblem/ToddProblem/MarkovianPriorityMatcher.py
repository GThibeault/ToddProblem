class MarkovianPriorityMatcher(object):

    def match(self, rankingMatrix, stationaryState):
        rankedStationary = sorted(
            enumerate(stationaryState), key=lambda s: s[1], reverse=True)

        pairs = []
        taken = {i: False for i in self.__getRankingRange(rankingMatrix)}

        for index, weight in rankedStationary:
            if taken[index]:
                continue

            rankedPreference = sorted(
                enumerate(rankingMatrix[index]), key=lambda s: s[1] if s[0] != index else len(rankingMatrix), reverse=False)

            firstAvailable = next(
                filter(lambda p: self.__isAvailable(p, taken), rankedPreference))[0]

            taken[index] = True
            taken[firstAvailable] = True

            pairs.append((index, firstAvailable))

        return pairs

    def __getRankingRange(self, rankingMatrix):
        return range(len(rankingMatrix))

    def __isAvailable(self, preference, taken):
        prefIndex, prefRanking = preference

        return not taken[prefIndex]
