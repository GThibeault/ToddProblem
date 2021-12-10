from MarkovianMatcherBase import MarkovianMatcherBase


class MarkovianPriorityMatcher(MarkovianMatcherBase):
    def match_pair(self, rankedPreference, taken):
        nextAvailable = next(
            filter(lambda p: not taken[p[0]], rankedPreference))

        return nextAvailable[0]
