from MatcherBase import MatcherBase


class WeightedMatcher(MatcherBase):
    def match_pair(self, taken, index, rankingMatrix, weights):
        availableRanking = [(i, r) for i, r in enumerate(
            rankingMatrix[index]) if not taken[i]]

        weightedMatches = [(i, self.__weightedMatch(
            index, i, r, rankingMatrix, weights)) for i, r in availableRanking]

        match = max(weightedMatches, key=lambda a: a[1])[0]

        return match

    def __weightedMatch(self, index, preferenceIndex, preference, rankingMatrix, weights):
        return preference * \
            weights[index] + \
            rankingMatrix[preferenceIndex][index] * \
            weights[preferenceIndex]
