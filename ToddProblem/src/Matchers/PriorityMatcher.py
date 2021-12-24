from Matchers.MatcherBase import MatcherBase


class PriorityMatcher(MatcherBase):
    def match_pair(self, taken, index, rankingMatrix, weights):
        firstAvailable = max(((i, x) for i, x in enumerate(
            rankingMatrix[index]) if not taken[i]), key=lambda p: p[1])

        return firstAvailable[0]
