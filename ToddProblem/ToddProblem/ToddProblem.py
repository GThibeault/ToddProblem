from StationaryState import *
from RankingMatrixMarkovizer import *
from RankingMatrixPreprocessor import *
from MarkovianPriorityMatcher import *
from numpy import array


class ToddProblemSolver(object):
    def solve(self, rankingMatrix):
        processedRankingMatrix = RankingMatrixPreprocessor.preprocess(
            rankingMatrix)
        markov = RankingMatrixMarkovizer.markovize(processedRankingMatrix)
        eigenvector = StationaryState.getStationaryState(markov)

        pairs = MarkovianPriorityMatcher.match(
            processedRankingMatrix, eigenvector)

        return pairs
