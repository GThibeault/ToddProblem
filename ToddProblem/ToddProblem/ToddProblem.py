from StationaryState import *
from RankingMatrixMarkovizer import *
from RankingMatrixPreprocessor import *
from MarkovianPriorityMatcher import *
from numpy import array

rankingMatrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]

processedRankingMatrix = RankingMatrixPreprocessor.preprocess(rankingMatrix)
markov = RankingMatrixMarkovizer.markovize(processedRankingMatrix)
eigenvector = StationaryState.getStationaryState(markov)

pairs = MarkovianPriorityMatcher.match(processedRankingMatrix, eigenvector)

print(pairs)
