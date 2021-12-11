from MarkovianMatcherBase import MarkovianMatcherBase


class MarkovianPriorityMatcher(MarkovianMatcherBase):
    def match_pair(self, taken, index, rankedPreferenceMatrix, rankedStationary):
        nextAvailable = next(
            filter(lambda p: not taken[p[0]], rankedPreferenceMatrix[index]))

        return nextAvailable[0]
