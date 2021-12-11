from MarkovianMatcherBase import MarkovianMatcherBase


class MarkovianBalancedMatcher(MarkovianMatcherBase):
    def match_pair(self, taken, index, rankedPreferenceMatrix, rankedStationary):
        reciprocalIndex = rankedStationary[-1-index][0]

        if taken[reciprocalIndex]:
            raise ValueError(
                f"Matching balanced pair already taken: {index} and reciprocal {reciprocalIndex}.")

        return reciprocalIndex
