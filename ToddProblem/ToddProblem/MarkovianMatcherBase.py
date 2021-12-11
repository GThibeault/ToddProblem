class MarkovianMatcherBase(object):

    def execute(self, rankingMatrix, stationaryState):
        rankedStationary = sorted(
            enumerate(stationaryState), key=lambda s: s[1], reverse=True)

        rankedPreferenceMatrix = map(lambda i: self.__getRankedPreferences(
            rankingMatrix, i), range(len(rankingMatrix)))

        pairs = []
        taken = {i: False for i in range(len(rankingMatrix))}

        for index, weight in self.__getIterFromRanking(rankedStationary):
            if taken[index]:
                continue

            matched = self.match_pair(
                taken, index, rankedPreferenceMatrix, rankedStationary)

            taken[index] = True
            taken[matched] = True

            pairs.append((index, matched))

        return pairs

    def __getIterFromRanking(self, ranking):
        return ranking

    def __getRankedPreferences(self, rankingMatrix, index):
        return sorted(
            enumerate(rankingMatrix[index]), key=lambda s: s[1] if s[0] != index else len(rankingMatrix), reverse=False)
