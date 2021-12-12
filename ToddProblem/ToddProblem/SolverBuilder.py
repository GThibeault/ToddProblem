from BalancedMatcher import *
from FlatWeighter import *
from WeightedMatcher import *
from RankingMatrixReverser import *
from Solver import Solver
from StationaryStateFinder import *
from RankingMatrixMarkovizer import *
from RankingMatrixSquarer import *
from PriorityMatcher import *
from Constants import *


class SolverBuilder(object):
    def build(self, config):
        preprocessors = self.__buildPreprocessors(config)
        weighters = self.__buildWeighters(config)
        matcher = self.__buildMatcher(config)

        solver = Solver(preprocessors, weighters, matcher)

        return solver

    def __buildPreprocessors(self, config):
        if Constants.preprocessor not in config:
            return [
                RankingMatrixSquarer(), RankingMatrixReverser()]

        decisionDict = {
            Constants.markov: lambda: [
                RankingMatrixSquarer(), RankingMatrixReverser()]
        }

        return self.__build(config, Constants.preprocessor, decisionDict, [])

    def __buildWeighters(self, config):
        decisionDict = {
            Constants.markov: lambda: [
                RankingMatrixMarkovizer(), StationaryStateFinder()],
            Constants.flat: lambda: [
                FlatWeighter()]
        }

        return self.__build(config, Constants.weighter, decisionDict, [])

    def __buildMatcher(self, config):
        decisionDict = {
            Constants.priority: lambda: PriorityMatcher(),
            Constants.balanced: lambda: BalancedMatcher(),
            Constants.weighted: lambda: WeightedMatcher(),
        }

        return self.__build(config, Constants.matcher, decisionDict, None)

    def __build(self, config, key, decisionDict, default):
        if config is not None and key in config:
            selectedPreprocessor = config[key]

            if selectedPreprocessor in decisionDict:
                return decisionDict[selectedPreprocessor]()

        return default
