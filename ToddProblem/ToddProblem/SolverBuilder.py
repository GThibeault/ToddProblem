from Solver import Solver
from StationaryStateFinder import *
from RankingMatrixMarkovizer import *
from RankingMatrixPreprocessor import *
from MarkovianPriorityMatcher import *
from Constants import Constants


class SolverBuilder(object):
    def build(self, config):
        preprocessors = self.__buildPreprocessors(config)
        weighters = self.__buildWeighters(config)
        matcher = self.__buildMatcher(config)

        solver = Solver(preprocessors, weighters, matcher)

        return solver

    def __buildPreprocessors(self, config):
        decisionDict = {
            Constants.markov: lambda: [RankingMatrixPreprocessor()]
        }

        return self.__build(config, Constants.preprocessor, decisionDict, [])

    def __buildWeighters(self, config):
        decisionDict = {
            Constants.markov: lambda: [
                RankingMatrixMarkovizer(), StationaryStateFinder()]
        }

        return self.__build(config, Constants.weighter, decisionDict, [])

    def __buildMatcher(self, config):
        decisionDict = {
            Constants.priority: lambda: MarkovianPriorityMatcher()
        }

        return self.__build(config, Constants.matcher, decisionDict, None)

    def __build(self, config, key, decisionDict, default):
        if config is not None and key in config:
            selectedPreprocessor = config[key]

            if selectedPreprocessor in decisionDict:
                return decisionDict[selectedPreprocessor]()

        return default
