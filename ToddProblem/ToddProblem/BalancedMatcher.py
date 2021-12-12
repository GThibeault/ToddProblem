from MatcherBase import MatcherBase


class BalancedMatcher(MatcherBase):
    def match_pair(self, taken, index, rankingMatrix, weights):
        rankedWeights = self.getIterFromWeights(weights)
        reciprocalIndex = rankedWeights[-1-index][0]

        if taken[reciprocalIndex]:
            raise ValueError(
                f"Matching balanced pair already taken: {index} and reciprocal {reciprocalIndex}.")

        return reciprocalIndex
