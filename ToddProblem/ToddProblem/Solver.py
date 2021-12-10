from functools import reduce


class Solver(object):
    def __init__(self, preprocessors, weighters, matcher):
        self.__preprocessors = self.__default(preprocessors, [])
        self.__weighters = self.__default(weighters, [])
        self.__matcher = matcher

    def __default(self, value, default):
        return value if value is not None else default

    def solve(self, rankingMatrix):
        processedRankingMatrix = reduce(lambda accum, preprocessor: preprocessor.execute(
            accum), self.__preprocessors, rankingMatrix)

        weight = reduce(lambda accum, weighter: weighter.execute(
            accum), self.__weighters, processedRankingMatrix)

        pairs = self.__matcher.execute(processedRankingMatrix, weight)

        return pairs
